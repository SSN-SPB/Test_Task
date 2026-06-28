# This code demonstrates how to search for files
# in the current directory that match a specific pattern
# (in this case, files with a .txt extension)
# using the pathlib library.
from pathlib import Path


def main():
    # Create Path objects
    file_path = Path("my_file.txt")
    directory_path = Path("my_directory")

    # Check existence of file/directory
    if file_path.exists():
        print(f"File {file_path} exists")
    else:
        print(f"File {file_path} does not exist and will be created")
        # Create file and write to it
        file_path.write_text("Hello, pathlib!")

    if directory_path.exists():
        print(f"Directory {directory_path} exists")
    else:
        print(f"Directory {directory_path} does not exist")

    if directory_path.is_dir():
        print(f"This is a directory")

    # Create directory
    directory_path.mkdir(
        parents=True, exist_ok=True
    )  # parents=True creates parent directories if needed, exist_ok=True prevents error if directory already exists

    if directory_path.exists():
        print(f"Directory {directory_path} exists")
    else:
        print(f"Directory {directory_path} does not exist")

    if directory_path.is_dir():
        print(f"This is a directory")

    # Read from file
    file_content = file_path.read_text()
    print(f"File content: {file_content}")

    # Copy file instead of renaming (preserve original)
    new_file_path = Path("my_new_file.txt")
    new_file_path.write_bytes(
        file_path.read_bytes()
    )  # copy file content instead of renaming to preserve original

    if directory_path.exists():
        print(f"Directory {directory_path} exists")
    else:
        print(f"Directory {directory_path} does not exist")

    if new_file_path.exists():
        print(f"New File {new_file_path} exists")
    else:
        print(f"New File {new_file_path} does not exist")

    # Delete files
    print(f"Deleting files: {file_path} and {new_file_path}")
    new_file_path.unlink()
    file_path.unlink()

    # Iterate over files in directory
    for file in directory_path.iterdir():
        print(file)

    # Get absolute path
    absolute_path = directory_path.resolve()
    print(f"Absolute path: {absolute_path}")

    # Create nested directories and a file
    nested_dir = Path("my_directory/nested/deeper")
    nested_dir.mkdir(parents=True, exist_ok=True)
    nested_file = nested_dir / "nested_file.txt"  # / is used to join paths
    nested_file.write_text("Content in nested file")

    file_content = nested_file.read_text()
    print(f"File content of the nested file: {file_content}")

    if directory_path.exists():
        print(f"Directory {nested_dir} exists")
    else:
        print(f"Directory {nested_dir} does not exist")

    import shutil

    # Remove directory and its contents
    print(f"Remove directory {directory_path} and its contents")
    # shutil.rmtree is used to remove non-empty directories
    shutil.rmtree(directory_path)


if __name__ == "__main__":
    main()
