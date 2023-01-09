#!/usr/bin/python3
def magic_string(i=[0]):  # array is evaluated once
    i[0] += 1  # crazy smart!, same object through out func call
    return f"BestSchool{', BestSchool' * (i[0] - 1)}"
