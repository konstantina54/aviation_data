import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta
from prefect_sqlalchemy import SqlAlchemyConnector



@task(log_prints=True, tags=["extract"], cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def extract_data(csv_name, table_name):

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)
    return df

@task(log_prints=True)
def transform_data(df):
    print(f"pre: landed planes count: {df['flight_status'].isin([0]).sum()}")
    df = df[df['flight_status'] != 'landed']
    print(f"post: landed planes count: {df['flight_status'].isin([0]).sum()}")
    return df

@task(log_prints=True, retries=3)
def load_data(table_name, df):
    connection_block = SqlAlchemyConnector.load("aviation-data-sync")
    with connection_block.get_connection(begin=False) as engine:
        df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
        df.to_sql(name=table_name, con=engine, if_exists='append')

@flow(name="Subflow", log_prints=True)
def log_subflow(table_name: str):
    print(f"Logging Subflow for: {table_name}")

@flow(name="Ingest Data")
def main_flow(table_name):

    csv_data = "/Users/admin/code/aviation_data/aviation_data.csv"
    log_subflow(table_name)
    raw_data = extract_data(csv_data, table_name)
    data = transform_data(raw_data)
    load_data(table_name, data)

if __name__ == '__main__':
    table_name = "aviation_data"

    main_flow(table_name)