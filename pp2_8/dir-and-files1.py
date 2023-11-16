import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all(path):
    all_items = os.listdir(path)
    return all_items

def main():
    specified_path = input()

    if os.path.exists(specified_path):
        print("\nDirectories:")
        print(list_directories(specified_path))

        print("\nFiles:")
        print(list_files(specified_path))

        print("\nAll Directories and Files:")
        print(list_all(specified_path))
    else:
        print("Specified path does not exist.")

if __name__ == "__main__":
    main()
