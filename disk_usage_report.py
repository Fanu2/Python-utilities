import psutil

def main():
    # Get disk usage information
    usage = psutil.disk_usage('/')
    print(f"Total Disk Space: {usage.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {usage.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {usage.free / (1024 ** 3):.2f} GB")
    print(f"Percentage Used: {usage.percent}%")

if __name__ == '__main__':
    main()
