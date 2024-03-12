from app.io.input import *
from app.io.output import *


def main():
    # Input text from console
    user_input = input_text()
    output_text("You entered: " + user_input)
    write_to_file("data/output.txt", user_input)

    # Read from file and output to console and another file
    file_content = read_from_file("data/somefile.txt")  # Ensure this file exists
    output_text("File content: " + file_content)
    write_to_file("data/output.txt", file_content)

    # Read from a CSV file using pandas and output to console and another file
    # Ensure 'somefile.csv' exists and is a valid CSV file
    df_content = read_from_file_with_pandas("data/somefile.csv").to_string()
    output_text("DataFrame content:\n" + df_content)
    write_to_file("data/output.txt", df_content)


if __name__ == "__main__":
    main()
