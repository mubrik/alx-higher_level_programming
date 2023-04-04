#!/usr/bin/python3
""" function that find peak in aray by chatgpt lol """


def find_peak(list_of_integers):
    """ implementation """
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize variables for binary search
    left = 0
    right = len(list_of_integers) - 1

    # Perform binary search to find a peak
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid+1]:
            left = mid + 1
        else:
            right = mid

    # Return the peak
    return list_of_integers[left]
