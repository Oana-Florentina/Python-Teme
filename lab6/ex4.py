import os
import sys

def count_files_by_extension(directory_path):
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            raise FileNotFoundError("Invalid directory path or directory does not exist")

        # Get all files in the directory
        files = os.listdir(directory_path)

        # Check if the directory is empty
        if not files:
            print(f"The directory '{directory_path}' is empty.")
            return

        extension_counts = {}

        # Count files for each extension
        for file in files:
            if os.path.isfile(os.path.join(directory_path, file)):
                file_extension = os.path.splitext(file)[1]
                extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        # Display the counts for each extension
        print("Number of files by extension:")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count}")

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
        count_files_by_extension(directory_path)
