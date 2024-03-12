import pytest
from app.io.input import read_from_file
from app.io.output import write_to_file

def test_read_from_file_exists():
    content = read_from_file("test_file.txt")
    assert content is not None


def test_read_from_file_content():
    expected_content = "Hello, world!"
    write_to_file("test_file.txt", expected_content, "w")
    content = read_from_file("test_file.txt")
    assert content == f"{expected_content}\n"


def test_read_from_file_no_file():
    with pytest.raises(FileNotFoundError):
        read_from_file("non_existent_file.txt")
