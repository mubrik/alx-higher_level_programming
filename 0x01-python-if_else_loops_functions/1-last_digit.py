#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
is_neg = number < 0
last_d = (abs(number) % 10)
""" txt = "and is 0" if last_d == 0 else "and is greater than 5" if\
  not is_neg and last_d > 5 else "and is less than 6 and not 0" """
# text
txt = None
if last_d == 0:
    txt = "and is 0"
elif not is_neg and last_d > 5:
    txt = "and is greater than 5"
else:
    txt = "and is less than 6 and not 0"
# to show neg sign
neg = '-' if is_neg and last_d != 0 else ''

print(f"Last digit of {number} is {neg}{last_d} {txt}")
