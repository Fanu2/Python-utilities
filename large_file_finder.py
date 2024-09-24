import os
import humanize

def find_large_files(directory, size_threshold):
    """
    Find files larger than the specified size threshold in the given directory.

    Args:
    directory (str): The directory to search for large files.
    size_threshold (int): The size threshold in bytes.

    Returns:
    List of tuples with file path and size in bytes.
    """
    large_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > size_threshold:
                    large_files.append((file_path, file_size))
            except OSError as e:
                print(f"Error accessing file {file_path}: {e}")

    return large_files

def main():
    directory = input("/home/jasvir/Documents/ ")
    size_threshold_mb = float(input("2 "))
    size_threshold_bytes = size_threshold_mb * 1024 * 1024

    large_files = find_large_files(directory, size_threshold_bytes)

    if large_files:
        print(f"\nFiles larger than {size_threshold_mb} MB:\n")
        for file_path, file_size in large_files:
            print(f"{file_path} - {humanize.naturalsize(file_size)}")
    else:
        print(f"No files larger than {size_threshold_mb} MB found.")

if __name__ == '__main__':
    main()
