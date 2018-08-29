#!/usr/bin/env python3
"""
    Purpose:
        You are given two non-empty linked lists representing two non-negative
        integers. The digits are stored in reverse order and each of
        their nodes contain a single digit. Add the two numbers and
        return it as a linked list.

        You may assume the two numbers do not contain any leading zero,
        except the number 0 itself.

        Example:
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
"""


def two_sum_brute(list_of_numbers, sum_value):
    """
    Purpose:
        Find first index position of numbers in a list that add
        up to the specified sum value
    Args:
        list_of_numbers (List of Ints): List of ints to see if they add up
            to the sum value
        sum_value (Integer): Sum value to search
    """

    if not list_of_numbers:
        return None
    elif len(list_of_numbers) < 2:
        return None

    for x in range(len(list_of_numbers)):
        for y in range(x + 1, len(list_of_numbers)):
            # print('{0} -> {1}'.format(x, y))
            if sum_value == list_of_numbers[x] + list_of_numbers[y]:
                return [x, y]

    return None


def two_sum_compliment(list_of_numbers, sum_value):
    """
    Purpose:
        Find first index position of numbers in a list that add
        up to the specified sum value
    Args:
        list_of_numbers (List of Ints): List of ints to see if they add up
            to the sum value
        sum_value (Integer): Sum value to search
    """

    if not list_of_numbers:
        return None
    elif len(list_of_numbers) < 2:
        return None

    known_keys = {}
    for x in range(len(list_of_numbers)):

        compliment = sum_value - list_of_numbers[x]
        if compliment in known_keys.keys():
            return [known_keys[compliment], x]
        else:
            known_keys[list_of_numbers[x]] = x

    return None


if __name__ == '__main__':
    sum_brute = two_sum([3,2,4], 6)
    sum_compliment = two_sum_compliment([3,2,4], 6)
    print(sum_brute)
    print(sum_compliment)

