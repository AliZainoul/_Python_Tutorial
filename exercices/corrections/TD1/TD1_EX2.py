import os

def list_files_with_size(starting_directory: str = "."):
    """Recursively list all files and directories, showing file sizes."""
    for root, dirs, files in os.walk(starting_directory):
        print(f"Directory: {root}")
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            print(f"    {file} - Size: {file_size} bytes")

def main():
    print("Listing all files and directories with sizes:")
    list_files_with_size()

if __name__ == "__main__":
    main()