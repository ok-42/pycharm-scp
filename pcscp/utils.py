WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


def convert_line_endings(input_file: str, output_file: str) -> None:
    """Replace CRLF (Windows) with LF (Unix).

    :param input_file: relative path to the original file with CRLF
    :param output_file: relative path to a new file with LF
    :return: None; creates a new file
    """

    with open(input_file, 'rb') as open_file:
        content = open_file.read()

    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

    with open(output_file, 'wb') as open_file:
        open_file.write(content)
