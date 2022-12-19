#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Write a function that divides element by element 2 lists."""
    if not my_list_1 or not my_list_2:
        return []
    result = 0
    new_list = [0 for num in range(list_length)]
    for index in range(list_length):
        try:
            a, b = my_list_1[index], my_list_2[index]
            if not isinstance(a, int) or not isinstance(b, int):
                raise TypeError
            result = a / b
        except (TypeError, IndexError, ZeroDivisionError, Exception) as ex:
            ty = type(ex)
            if ty is TypeError:
                print("wrong type")
            elif ty is IndexError:
                print("out of range")
            elif ty is ZeroDivisionError:
                print("division by 0")
            result = 0
        finally:
            new_list[index] = result
    return new_list
