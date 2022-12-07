#!/usr/bin/python3


def roman_to_int(roman_string: str):
    """ Create a function def roman_to_int(roman_string): that converts a
    Roman numeral to an integer. """
    rom_to_num = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    if not roman_string:
        return 0
    total = 0
    for index, letter in enumerate(roman_string):
        # first part of string
        if not index:
            # using get and default value 0 cause alx loves trolling
            total += rom_to_num.get(letter, 0)
            continue
        # check if larger than previous
        prev = rom_to_num.get(roman_string[index - 1], 0)
        curr = rom_to_num.get(letter, 0)
        if curr > prev:
            # remove previous from total, then add differnce of curr
            total = (total - prev) + (curr - prev)
        else:
            total += curr
    return total
