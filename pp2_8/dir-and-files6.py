import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the content of file {file_name}")

    print("Text files generated successfully.")

if __name__ == "__main__":
    generate_text_files()