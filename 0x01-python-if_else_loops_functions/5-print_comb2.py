#!/usr/bin/python3

for i in range(0, 100):
    # 02 0-padding, 2-width
    print("{:02}".format(i), end=", " if i < 99 else "\n")
