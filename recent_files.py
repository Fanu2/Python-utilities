import os
import datetime


def get_recent_files(directory, days=7):
    """
    Get files in the specified directory that have been modified in the last 'days' days.
    """
    current_time = datetime.datetime.now()
    recent_files = []

    # Iterate over files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file's last modified time
            file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

            # Check if the file was modified within the last 'days' days
            if (current_time - file_mod_time).days <= days:
                recent_files.append(file_path)

    return recent_files


def main():
    # Specify the directory to check
    directory = '.'  # Current directory, change as needed
    days = 7  # Number of days to check

    recent_files = get_recent_files(directory, days)

    if recent_files:
        print(f"Files modified in the last {days} days:")
        for file in recent_files:
            print(file)
    else:
        print(f"No files modified in the last {days} days.")


if __name__ == '__main__':
    main()
