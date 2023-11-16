def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List has been written to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    data_to_write = ["apple", "banana", "orange", "grape", "kiwi"]
    file_path = input()

    write_list_to_file(file_path, data_to_write)

if __name__ == "__main__":
    main()