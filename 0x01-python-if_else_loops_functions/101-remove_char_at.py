#!/usr/bin/python3

def remove_char_at(str: str, n):
    if n < 0 or len(str) < n:
        return str
    rep = str[n]
    return str.replace(rep, '')
