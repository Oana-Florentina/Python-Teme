import os
import sys

def calculate_total_file_size(directory_path):
    total_size = 0

    try:
        # Check if the directory exists
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            raise FileNotFoundError("Invalid directory path or directory does not exist")

        # Iterate through the directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Get the size of each file and add it to the total size
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                except OSError as e:
                    print(f"Error accessing {file_path}: {e}")

        print(f"Total size of all files in '{directory_path}': {total_size} bytes")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py directory_path")
    else:
        directory_path = sys.argv[1]
        calculate_total_file_size(directory_path)
