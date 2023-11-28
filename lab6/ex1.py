import os
import sys

def read_files_in_directory(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            raise FileNotFoundError("Invalid directory path or directory does not exist")

        for file_name in os.listdir(directory_path):
            if file_name.endswith(file_extension):
                file_path = os.path.join(directory_path, file_name)
                try:
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {file_name}:")
                        print(contents)
                        print("-" * 30)
                except Exception as e:
                    print(f"Error reading {file_name}: {e}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py directory_path file_extension")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        read_files_in_directory(directory_path, file_extension)
