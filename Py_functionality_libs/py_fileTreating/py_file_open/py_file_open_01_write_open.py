"""File operations demonstration with best practices."""

from pathlib import Path
from typing import Optional

HELLO_MESSAGE = "Hello world"
FILE_NAME = "tested_file.txt"


def create_file_with_text(content_message: str, name_of_file: str) -> int:
    """
    Create a file and write content to it.

    Args:
        content_message: The text to write to the file
        name_of_file: The file path to create

    Returns:
        The number of characters written

    Raises:
        IOError: If file creation/writing fails
    """
    try:
        with open(name_of_file, "w", encoding="utf-8") as new_file:
            bytes_written = new_file.write(content_message)
        return bytes_written
    except IOError as e:
        print(f"Error writing to file: {e}")
        raise


def read_file_content(name_of_file: str) -> Optional[str]:
    """
    Read and return file content.

    Args:
        name_of_file: The file path to read

    Returns:
        The file content as a string, or None if read fails

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file reading fails
    """
    try:
        with open(name_of_file, "r", encoding="utf-8") as current_file:
            content = current_file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {name_of_file}")
        raise
    except IOError as e:
        print(f"Error reading file: {e}")
        raise


def main(file_path: str = FILE_NAME, cleanup: bool = True) -> None:
    """
    Main function demonstrating file operations.

    Args:
        file_path: Path to the test file
        cleanup: Whether to delete the file after reading
    """
    try:
        # Create file and get bytes written
        total_symbols_in_file = create_file_with_text(HELLO_MESSAGE, file_path)
        print(f"Bytes written: {total_symbols_in_file}")

        # Read and display content
        content = read_file_content(file_path)
        print(f"File content: {content}")

        # Cleanup
        if cleanup and Path(file_path).exists():
            Path(file_path).unlink()
            print(f"Cleaned up: {file_path}")
    except Exception as e:
        print(f"Error in main: {e}")
        raise


if __name__ == "__main__":
    main()
