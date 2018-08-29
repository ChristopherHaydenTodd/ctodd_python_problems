#!/usr/bin/env python3
"""
    Purpose:
        The string "PAYPALISHIRING" is written in a zigzag pattern on a
        given number of rows like this: (you may want to display this
        pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion
        given a number of rows:

        convert_to_zigzag(string normal_string, int number_of_rows)

        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"

        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:

        P     I    N
        A   L S  I G
        Y A   H R
        P     I

        P       H
        A     S I
        Y   I   R
        P L     I G
        A       N


        P         R
        A       I I
        Y     H   N
        P   S     G
        A I
        L

"""


def convert_to_zigzag(normal_string, number_of_rows=3):
    """
    Purpose:
        Convert string into zigzagged representation based on the
        number of rows provided (default 3).
    Args:
        normal_string (String): String to convert into zigzag
        number_of_rows (Integer): Rows (Vertical) to zigzag a string
    """

    # if string is none or empty, return ''
    if not normal_string or number_of_rows <= 0 :
        return ''

    # If string is less than the size of the rows, nothing to ZigZag
    if len(normal_string) <= number_of_rows:
        return normal_string

    # Create ZigZag List Form
    string_rows = []
    for row in range(number_of_rows):
        string_rows.append([])

    # Create ZigZag Lists
    row_iterator = 0
    row_direction = 1
    for character in normal_string:
        string_rows[row_iterator].append(character)

        row_iterator += row_direction
        if row_iterator >= number_of_rows or row_iterator < 0:
            row_direction *= -1
            row_iterator += row_direction + row_direction

    # Loop Through ZigZag and Return Result
    final_string = ''
    for row in range(number_of_rows):
        final_string += ''.join(string_rows[row])

    return final_string


if __name__ == '__main__':
    zigzag_1 = convert_to_zigzag('PAYPALISHIRING', number_of_rows=3)
    zigzag_2 = convert_to_zigzag('PAYPALISHIRING', number_of_rows=4)

    print(zigzag_1)
    print(zigzag_2)

