import os

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            print(f"File '{file_path}' exists.")

            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            else:
                print(f"File '{file_path}' is not writable. Cannot delete.")
        else:
            print(f"File '{file_path}' does not exist. Cannot delete.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input()
    delete_file(file_path)

if __name__ == "__main__":
    main()