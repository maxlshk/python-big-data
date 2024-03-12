def output_text(text):
    """
    Prints the provided text to the console.

    Parameters:
        text (str): The text to be printed.
    """
    print(text)


def write_to_file(filename, content, mode='a'):
    """
    Writes or appends the given content to a file, based on the specified mode in UTF-8 encoding.

    Parameters:
        filename (str): The name of the file where the content will be written or appended.
        content (str): The content to write or append to the file.
        mode (str): The mode in which to open the file. 'w' for write (default, overwrites file),
                    'a' for append (adds to the end of the file).
    """
    if mode not in ['w', 'a']:
        raise ValueError("Invalid mode. Use 'w' for write or 'a' for append.")

    with open(filename, mode, encoding='utf-8') as file:
        file.write(content + "\n")




