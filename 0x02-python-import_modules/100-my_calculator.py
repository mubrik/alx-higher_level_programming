#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div


def args_is_valid():
    """check if args are valid"""
    return (len(sys.argv) == 4)


def is_valid_operator(str):
    """check if operator is valid"""
    return (str == "+" or str == "*" or str == "/" or str == "-")


def get_operator(str):
    """gets the function handling a valid operator

    Args:
        str (_type_): valid operator

    Returns:
        function: a funct that handles an operation
    """
    op_to_func = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }

    return op_to_func[str]


def main():
    """ logic goes here"""
    if not args_is_valid():
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    op = sys.argv[2]
    if not is_valid_operator(op):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    calculate = get_operator(op)
    a = sys.argv[1]
    b = sys.argv[3]
    print("{} {} {} = {}".format(a, op, b, calculate(int(a), int(b))))


if __name__ == "__main__":
    main()
