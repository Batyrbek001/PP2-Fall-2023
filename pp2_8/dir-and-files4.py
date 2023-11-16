def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"Number of lines in '{file_path}': {line_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input()
    count_lines(file_path)

if __name__ == "__main__":
    main()