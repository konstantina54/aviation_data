# def most_frequent(arr):
#     freq_dict = {}
#     for num in arr:
#         if num in freq_dict:
#             # If the number is already in the dictionary, increment its frequency by 1
#             freq_dict[num] += 1
#         else:
#             # If the number is not in the dictionary, add it with an initial frequency of 1
#             freq_dict[num] = 1
#     # Use the max function to find the key with the maximum value in the dictionary
#     print(freq_dict)
#     return max(freq_dict, key=freq_dict.get)

# arr = [97, 9, 38, 94, 53, 16, 9, 34, 62, 62, 2, 62, 51, 80, 44]

# print(most_frequent(arr))

def to_camel_case(text):
    if '_' in text and '-' in text:
        text = text.replace('-', ' ').replace('_', ' ')
        text = text.split()
        print(type(text))
    elif '_' in text:
        text = text.split('_')
        print(type(text))
    elif '-' in text:
        text = text.split('-')
    print(text)
    count = 0
    x= ''
    for i in text:
#         count +=1
        if count == 0:
            print(i+'this')
            x = i
            count +=1
        else:
            res = i.capitalize()
            print(res)
            x= x+res
    print(x)
    return x



to_camel_case('A_pippi-Was-pippi')
to_camel_case('the_stealth_warrior')
to_camel_case('A-B-C')