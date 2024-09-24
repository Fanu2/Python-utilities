import os
import datetime


def get_unused_files(directory, days=30):
    """
    Get files in the specified directory that haven't been accessed in the last 'days' days.
    """
    current_time = datetime.datetime.now()
    unused_files = []

    # Iterate over files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file's last accessed time
            file_access_time = datetime.datetime.fromtimestamp(os.path.getatime(file_path))

            # Check if the file hasn't been accessed within the last 'days' days
            if (current_time - file_access_time).days > days:
                unused_files.append(file_path)

    return unused_files


def cleanup_files(files):
    """
    Delete the specified files.
    """
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")


def main():
    # Specify the directory to check
    directory = '.'  # Current directory, change as needed
    days = 30  # Number of days to check

    unused_files = get_unused_files(directory, days)

    if unused_files:
        print(f"Cleaning up files not accessed in the last {days} days:")
        cleanup_files(unused_files)
    else:
        print(f"No files found that haven't been accessed in the last {days} days.")


if __name__ == '__main__':
    main()
