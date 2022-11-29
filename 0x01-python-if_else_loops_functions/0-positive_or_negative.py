#!/usr/bin/python3
import random

number = random.randint(-10, 10)
txt = "is zero" if number == 0 else "is negative" if\
  number < 0 else "is positive"

print(f"{number} {txt}")
