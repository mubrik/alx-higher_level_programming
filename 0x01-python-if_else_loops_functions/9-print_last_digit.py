#!/usr/bin/python3


def get_last_digit(num):
    return (abs(num) % 10)


def print_last_digit(number):
    last_d = get_last_digit(number)
    print(last_d, end="")
    return last_d
