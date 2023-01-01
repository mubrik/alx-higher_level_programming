#!/usr/bin/python3
""" This is text_indentation module

The module supplies one function, text_indentation().

>>> text_indentation("hello?")
hello?

"""


def text_indentation(text):
    """ Write a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    >>> text_indentation("hello?")
    hello?

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    re = __import__("re")
    print(re.sub("[.?:][ ]*", lambda x: f"{x.group(0).strip()}\n\n", text),
          end="")
