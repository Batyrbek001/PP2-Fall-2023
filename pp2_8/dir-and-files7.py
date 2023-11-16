def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()

            with open(destination_path, 'w') as destination_file:
                destination_file.write(content)

        print(f"Contents copied from '{source_path}' to '{destination_path}'.")
    except FileNotFoundError:
        print(f"File '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_path = input()
    destination_path = input()

    copy_file(source_path, destination_path)

if __name__ == "__main__":
    main()