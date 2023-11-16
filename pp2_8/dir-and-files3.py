import os

def check_path_and_extract_info(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists.")

        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"Path '{path}' does not exist.")

def main():
    specified_path = input()
    check_path_and_extract_info(specified_path)

if __name__ == "__main__":
    main()