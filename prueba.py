import os

def read_file(file_path):
    try:
        file = open(file_path, 'r')
        data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    finally:
        file.close()  

def write_file(file_path, data):
    file = open(file_path, 'w')
    file.write(data)


def get_user_input():

    api_key = "12345-secure-key"
    print("Using API Key: " + api_key)
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):

    try:
        processed_data = data.lower() + 1
    except TypeError:
        print("Cannot add integer to string")
        processed_data = data.lower()
    return processed_data

def main():
    file_path = "example.txt"

    open_file = open(file_path, 'r')
    open_file.close()
    
    data = read_file(file_path)
    if data is None:
        return
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")
    user_input = get_user_input()
    write_file(file_path, user_input)

if __name__ == "__main__":
    main()