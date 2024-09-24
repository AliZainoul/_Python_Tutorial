import sys

def compare_python_version(required_version: str):
    """Compare current Python version with the required version."""
    current_version = sys.version_info
    required_version_tuple = tuple(map(int, required_version.split(".")))
    
    if current_version < required_version_tuple:
        print(f"Your Python version {sys.version} is older than {required_version}. Consider updating.")
    else:
        print(f"Your Python version {sys.version} is up to date.")

def main():
    required_version = input("Enter the required Python version (e.g., 3.8): ")
    compare_python_version(required_version)

if __name__ == "__main__":
    main()
