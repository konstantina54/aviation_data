✈️ Aviation Data Ingestion & Processing Pipeline
📖 Overview

This project implements a data engineering pipeline designed to ingest, process, and store aviation-related data. Utilizing Python, the pipeline reads raw aviation data, performs necessary transformations, and stores the cleaned data in a PostgreSQL database for further analysis or application use.
🧰 Tech Stack

    Language: Python 3.x

    Database: PostgreSQL

    Libraries: pandas, sqlalchemy, psycopg2

    Others: dotenv for environment variable management

📂 Project Structure

aviation_data/
├── aviation_data_ingest.py   # Handles data ingestion and storage
├── functions.py              # Contains helper functions for data processing
├── main.py                   # Entry point to run the pipeline
├── practise.py               # Script for testing and experimentation
├── requirements.txt          # Python dependencies
├── .gitignore                # Specifies files to ignore in version control
└── README.md                 # Project documentation

⚙️ Setup Instructions

    Clone the Repository:

git clone https://github.com/konstantina54/aviation_data.git
cd aviation_data

Create a Virtual Environment:

python3 -m venv venv
source venv/bin/activate

Install Dependencies:

pip install -r requirements.txt

Configure Environment Variables:

Create a .env file in the root directory and add your PostgreSQL credentials:

DB_HOST=your_host
DB_PORT=your_port
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password

Run the Pipeline:

    python main.py

🛠️ Features

    Data Ingestion: Reads raw aviation data from specified sources.

    Data Transformation: Cleans and transforms data for consistency and accuracy.

    Database Storage: Stores processed data into a PostgreSQL database.

    Modular Design: Separation of concerns with dedicated scripts for ingestion, processing, and utility functions.

🧪 Testing

To test individual components or the entire pipeline, you can use the practise.py script:

python practise.py

This script is intended for experimentation and validation of functions during development.
📈 Future Enhancements

    Data Validation: Implement stricter validation rules to ensure data quality.

    Logging: Integrate logging to monitor pipeline execution and errors.

    Dockerization: Containerize the application for easier deployment.

    CI/CD Integration: Set up continuous integration and deployment workflows.
