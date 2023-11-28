import os

def rename_files_with_sequential_prefix(directory_path):
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            raise FileNotFoundError("Invalid directory path or directory does not exist")

        # Get all files in the directory
        files = os.listdir(directory_path)

        # Filter out only files (not directories)
        files = [file for file in files if os.path.isfile(os.path.join(directory_path, file))]

        # Sort files alphabetically
        files.sort()

        # Rename files with sequential numbering
        for index, file_name in enumerate(files, start=1):
            file_extension = os.path.splitext(file_name)[1]  # Get file extension
            new_file_name = f"file{index}{file_extension}"
            old_file_path = os.path.join(directory_path, file_name)
            new_file_path = os.path.join(directory_path, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {file_name} to {new_file_name}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = "/home/florentina/Desktop"  # Replace with your directory path
    rename_files_with_sequential_prefix(directory_path)
