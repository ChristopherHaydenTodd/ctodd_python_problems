#!/usr/bin/env python3
"""
    Purpose:
        Test the zigzag_conversion
"""

# Project Libraries
from bin.zigzag_conversion import convert_to_zigzag


def test_null_string():
    """
        Purpose:
            Test Null and '' Strings
    """

    assert '' == convert_to_zigzag(None, number_of_rows=5)
    assert '' == convert_to_zigzag('', number_of_rows=5)


def test_rows_zero():
    """
        Purpose:
            Test Rows = 0 or Negative
    """

    assert '' == convert_to_zigzag('TESTING', number_of_rows=0)


def test_string_less_than_rows():
    """
        Purpose:
            Test Strings Where Rows are less than
            the length of the string
    """

    assert 'TESTING' == convert_to_zigzag('TESTING', number_of_rows=10)
    assert 'TESTING' == convert_to_zigzag('TESTING', number_of_rows=11)
    assert 'TESTING' == convert_to_zigzag('TESTING', number_of_rows=12)
    assert 'TESTING' == convert_to_zigzag('TESTING', number_of_rows=13)
    assert 'TESTING' == convert_to_zigzag('TESTING', number_of_rows=14)
    assert 'TESTING' == convert_to_zigzag('TESTING', number_of_rows=15)
    assert 'TESTING' == convert_to_zigzag('TESTING', number_of_rows=16)


def test_normal_execution():
    """
        Purpose:
            Test Strings Properly Converted to ZigZag form
    """

    assert 'PAHNAPLSIIGYIR' == convert_to_zigzag(
        'PAYPALISHIRING', number_of_rows=3
    )

    assert 'PINALSIGYAHRPI' == convert_to_zigzag(
        'PAYPALISHIRING', number_of_rows=4
    )
