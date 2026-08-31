"""Pytest tests for py_file_open_01_write_open module."""

import os
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

# Import the functions to test
from py_file_open_01_write_open import (
    HELLO_MESSAGE,
    create_file_with_text,
    main,
    read_file_content,
)


class TestCreateFileWithText:
    """Tests for create_file_with_text function."""

    def test_create_file_with_text_success(self):
        """Test successful file creation with content."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "test.txt"
            content = "Test content"

            bytes_written = create_file_with_text(content, str(test_file))

            assert test_file.exists()
            assert bytes_written == len(content)
            assert test_file.read_text(encoding="utf-8") == content

    def test_create_file_with_empty_content(self):
        """Test creating a file with empty content."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "empty.txt"

            bytes_written = create_file_with_text("", str(test_file))

            assert test_file.exists()
            assert bytes_written == 0
            assert test_file.read_text(encoding="utf-8") == ""

    def test_create_file_with_special_characters(self):
        """Test file creation with special characters and Unicode."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "special.txt"
            content = "Special chars: éàü 中文 Emoji: 🚀\nNewline test"

            create_file_with_text(content, str(test_file))

            assert test_file.exists()
            assert test_file.read_text(encoding="utf-8") == content

    def test_create_file_with_multiline_content(self):
        """Test file creation with multiline content."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "multiline.txt"
            content = "Line 1\nLine 2\nLine 3\n"

            bytes_written = create_file_with_text(content, str(test_file))

            assert bytes_written > 0
            assert test_file.read_text(encoding="utf-8") == content

    def test_create_file_overwrites_existing(self):
        """Test that creating a file overwrites existing content."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "overwrite.txt"

            # Write initial content
            create_file_with_text("Original content", str(test_file))
            assert test_file.read_text(encoding="utf-8") == "Original content"

            # Overwrite with new content
            create_file_with_text("New content", str(test_file))
            assert test_file.read_text(encoding="utf-8") == "New content"

    def test_create_file_in_nonexistent_directory_fails(self):
        """Test that creating a file in a non-existent directory fails."""
        nonexistent_path = "/nonexistent/path/to/file.txt"

        with pytest.raises(IOError):
            create_file_with_text("content", nonexistent_path)

    def test_create_file_with_large_content(self):
        """Test file creation with large content."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "large.txt"
            content = "x" * 1_000_000  # 1 MB of text

            bytes_written = create_file_with_text(content, str(test_file))

            assert bytes_written == len(content)
            assert test_file.read_text(encoding="utf-8") == content


class TestReadFileContent:
    """Tests for read_file_content function."""

    def test_read_file_content_success(self):
        """Test successful file reading."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "read_test.txt"
            content = "Read test content"
            test_file.write_text(content, encoding="utf-8")

            read_content = read_file_content(str(test_file))

            assert read_content == content

    def test_read_empty_file(self):
        """Test reading an empty file."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "empty_read.txt"
            test_file.write_text("", encoding="utf-8")

            read_content = read_file_content(str(test_file))

            assert read_content == ""

    def test_read_file_with_special_characters(self):
        """Test reading file with special characters."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "special_read.txt"
            content = "Special: éàü 中文 🚀\nMultiline"
            test_file.write_text(content, encoding="utf-8")

            read_content = read_file_content(str(test_file))

            assert read_content == content

    def test_read_nonexistent_file_raises_error(self):
        """Test that reading non-existent file raises FileNotFoundError."""
        nonexistent_file = "/nonexistent/file.txt"

        with pytest.raises(FileNotFoundError):
            read_file_content(nonexistent_file)

    def test_read_preserves_formatting(self):
        """Test that file reading preserves original formatting."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "format.txt"
            content = "Line 1\n\nLine 3 with  spaces\n\tTabbed line\n"
            test_file.write_text(content, encoding="utf-8")

            read_content = read_file_content(str(test_file))

            assert read_content == content

    def test_read_large_file(self):
        """Test reading a large file."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "large_read.txt"
            content = "x" * 1_000_000
            test_file.write_text(content, encoding="utf-8")

            read_content = read_file_content(str(test_file))

            assert len(read_content) == 1_000_000
            assert read_content == content


class TestCreateAndReadIntegration:
    """Integration tests combining create and read operations."""

    def test_create_then_read_returns_same_content(self):
        """Test that reading a created file returns the same content."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "integration.txt"
            original_content = "Integration test content"

            bytes_written = create_file_with_text(
                original_content, str(test_file)
            )
            read_content = read_file_content(str(test_file))

            assert bytes_written == len(original_content)
            assert read_content == original_content

    def test_create_read_cycle_with_different_encodings_edge_case(self):
        """Test create/read cycle with various content types."""
        with TemporaryDirectory() as temp_dir:
            test_cases = [
                ("Simple ASCII", "Simple ASCII"),
                ("Numbers", "1234567890"),
                ("Punctuation", "!@#$%^&*()_+-=[]{}|;:',.<>?/"),
                ("Mixed", "Hello123!@#世界 🌍"),
            ]

            for name, content in test_cases:
                test_file = Path(temp_dir) / f"test_{name}.txt"
                create_file_with_text(content, str(test_file))
                read_content = read_file_content(str(test_file))
                assert read_content == content, f"Failed for: {name}"

    def test_create_read_with_constant(self):
        """Test that create/read works with the module constant."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "constant.txt"

            create_file_with_text(HELLO_MESSAGE, str(test_file))
            read_content = read_file_content(str(test_file))

            assert read_content == HELLO_MESSAGE
            assert read_content == "Hello world"


class TestMainFunction:
    """Tests for the main function."""

    def test_main_creates_and_reads_file(self, capsys):
        """Test main function creates and reads file successfully."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "main_test.txt"

            main(file_path=str(test_file), cleanup=False)

            captured = capsys.readouterr()
            assert str(len(HELLO_MESSAGE)) in captured.out
            assert HELLO_MESSAGE in captured.out
            assert test_file.exists()

    def test_main_with_cleanup_removes_file(self):
        """Test main function removes file when cleanup=True."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "cleanup_test.txt"

            main(file_path=str(test_file), cleanup=True)

            assert not test_file.exists()

    def test_main_without_cleanup_keeps_file(self):
        """Test main function keeps file when cleanup=False."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "no_cleanup_test.txt"

            main(file_path=str(test_file), cleanup=False)

            assert test_file.exists()
            assert test_file.read_text(encoding="utf-8") == HELLO_MESSAGE

    def test_main_displays_byte_count(self, capsys):
        """Test main function displays correct byte count."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "byte_test.txt"

            main(file_path=str(test_file), cleanup=False)

            captured = capsys.readouterr()
            expected_bytes = len(HELLO_MESSAGE)
            assert f"Bytes written: {expected_bytes}" in captured.out

    def test_main_with_nonexistent_directory_raises_error(self):
        """Test main function raises error for non-existent directory."""
        nonexistent_path = "/nonexistent/path/file.txt"

        with pytest.raises(IOError):
            main(file_path=nonexistent_path, cleanup=False)

    def test_main_default_parameters(self, capsys):
        """Test main function with default parameters."""
        with TemporaryDirectory() as temp_dir:
            original_dir = os.getcwd()
            try:
                os.chdir(temp_dir)

                # main() with defaults should use "tested_file.txt"
                # and cleanup=True (default)
                main()

                captured = capsys.readouterr()
                assert "Bytes written:" in captured.out
            finally:
                os.chdir(original_dir)


class TestEdgeCases:
    """Tests for edge cases and error conditions."""

    def test_file_with_only_whitespace(self):
        """Test file creation with only whitespace."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "whitespace.txt"
            content = "   \n\t\n   "

            bytes_written = create_file_with_text(content, str(test_file))
            read_content = read_file_content(str(test_file))

            assert bytes_written > 0
            assert read_content == content

    def test_file_with_very_long_line(self):
        """Test file with a very long single line."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "long_line.txt"
            content = "a" * 10000  # 10k chars in one line

            create_file_with_text(content, str(test_file))
            read_content = read_file_content(str(test_file))

            assert read_content == content

    def test_file_with_null_like_content(self):
        """Test file with content that looks like null values."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "null_like.txt"
            content = "None\nNull\nnull\nNULL\n"

            create_file_with_text(content, str(test_file))
            read_content = read_file_content(str(test_file))

            assert read_content == content

    def test_file_permissions_error_on_read(self):
        """Test that permission errors are handled on read (Unix only)."""
        # Skip on Windows as permission handling is different
        if os.name == "nt":
            pytest.skip("File permissions work differently on Windows")

        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "permission_test.txt"
            test_file.write_text("content", encoding="utf-8")

            # Remove read permissions
            os.chmod(test_file, 0o000)

            try:
                with pytest.raises(IOError):
                    read_file_content(str(test_file))
            finally:
                # Restore permissions for cleanup
                os.chmod(test_file, 0o644)


class TestByteCountAccuracy:
    """Tests to verify byte count accuracy."""

    def test_ascii_byte_count(self):
        """Test byte count for ASCII characters."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "ascii.txt"
            content = "ASCII text"  # 10 bytes

            bytes_written = create_file_with_text(content, str(test_file))

            assert bytes_written == 10

    def test_multibyte_character_byte_count(self):
        """Test character count for multi-byte UTF-8 characters.

        Python counts characters, not bytes.
        """
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "multibyte.txt"
            content = "你好"  # 2 Chinese characters returned as 2 by write()

            bytes_written = create_file_with_text(content, str(test_file))

            # Python's write() returns character count, not byte count
            assert bytes_written == 2

    def test_mixed_content_byte_count(self):
        """Test character count with mixed ASCII and multi-byte characters."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "mixed.txt"
            content = "Hello世界"  # 7 characters total

            bytes_written = create_file_with_text(content, str(test_file))

            # Python's write() returns character count
            assert bytes_written == 7


class TestFileNamingAndPaths:
    """Tests for different file naming and path scenarios."""

    def test_file_with_special_characters_in_name(self):
        """Test file operations with special characters in filename."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "test_file-2024_v1.2.txt"
            content = "Special filename"

            create_file_with_text(content, str(test_file))
            read_content = read_file_content(str(test_file))

            assert read_content == content

    def test_file_with_dot_prefix(self):
        """Test file operations with dot-prefixed filenames."""
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / ".hidden"
            content = "Hidden file"

            create_file_with_text(content, str(test_file))
            read_content = read_file_content(str(test_file))

            assert read_content == content

    def test_file_in_nested_directory(self):
        """Test file operations in nested directories."""
        with TemporaryDirectory() as temp_dir:
            nested_dir = Path(temp_dir) / "level1" / "level2"
            nested_dir.mkdir(parents=True)
            test_file = nested_dir / "nested.txt"
            content = "Nested file"

            create_file_with_text(content, str(test_file))
            read_content = read_file_content(str(test_file))

            assert read_content == content


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
