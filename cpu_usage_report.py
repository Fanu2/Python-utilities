import psutil


def main():
    # Get CPU usage information
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Number of Logical CPUs: {cpu_count}")


if __name__ == '__main__':
    main()
