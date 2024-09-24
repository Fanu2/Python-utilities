# file_organizer.py script

def main():
    pass

if __name__ == '__main__':
    main()
import os
import shutil

def organize_files(directory):
    """
    Organize files in the specified directory into subdirectories based on file extensions.
    """
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file extension
            _, ext = os.path.splitext(file_name)
            ext = ext[1:]  # Remove the leading dot

            # Skip files without an extension
            if not ext:
                ext = "no_extension"

            # Create a directory for the extension if it doesn't exist
            ext_dir = os.path.join(directory, ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)

            # Move the file to the appropriate directory
            shutil.move(file_path, os.path.join(ext_dir, file_name))
            print(f"Moved {file_name} to {ext_dir}")

def main():
    # Specify the directory to organize
    directory = '/home/jasvir/Documents/Princess Rosa/Rosa/'  # Current directory, change as needed
    organize_files(directory)

if __name__ == '__main__':
    main()
