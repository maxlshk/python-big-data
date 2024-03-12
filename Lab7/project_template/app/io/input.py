import pandas


def input_text():
    """
    Prompts the user to input text from the console.

    Returns:
        str: The text input by the user.
    """
    text = input("Enter text: ")
    return text


def read_from_file(filename):
    """
    Reads the contents of a file using built-in Python functions in UTF-8 encoding.

    Parameters:
        filename (str): The name of the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_with_pandas(filename):
    """
    Reads data from a CSV file into a pandas DataFrame.

    This function uses the pandas library to read a CSV file in UTF-8 and
    returns the data as a DataFrame. This is useful for further data
    manipulation and analysis using pandas.

    Parameters:
        filename (str): The name of the CSV file to be read.

    Returns:
        DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    df = pandas.read_csv(filename, encoding='utf-8')
    return df
