#!/usr/bin/python3
"""Multiplies 2 matrixes
"""


def validate_num_or_raise(num=None, name="m_a"):
    """ Checks if a num is a num or float, raise oterwise"""
    if isinstance(num, (int, float)):
        return True
    raise TypeError("{} should contain only integers or floats".format(name))


def validate_list_or_raise(mat=None, name="m_a"):
    """ Checks if a list of list and not empty """
    if not isinstance(mat, list):
        raise TypeError("{} must be a list".format(name))
    prev_len = 0
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("{} must be a list of lists".format(name))
        if not row:
            raise ValueError("{} can't be empty".format(name))
        if not prev_len:
            prev_len = len(row)
        else:
            if prev_len != len(row):
                _str = "each row of {} must be of the same size".format(name)
                raise TypeError(_str)
    if not mat:
        raise ValueError("{} can't be empty".format(name))
    return True


def matrix_mul(m_a, m_b):
    """Write a function that multiplies 2 matrices"""
    # initial checks
    """ a, b = isinstance(m_a, list), isinstance(m_b, list)
    if not a or not b:
        raise TypeError(f"{'m_a' if not a else 'm_b'} must be a list")
    b_rows_l = len(m_b)
    a_col_len = len(m_a[0]) """
    # validate
    validate_list_or_raise(m_a)
    validate_list_or_raise(m_b, "m_b")
    # all valid, get a row len and col len
    a_rows_l, a_col_l, b_row_l = len(m_a), len(m_a[0]), len(m_b)
    b_col_l = len(m_b[0])
    # check a col == b row
    if a_col_l != b_row_l:
        raise ValueError("m_a and m_b can't be multiplied")
    # create new matrix
    new_matrix = [[] for _ in range(a_rows_l)]
    # iterate 'new matrix' rows then column
    for i in range(a_rows_l):
        # get curr row in mat a
        a_row = m_a[i]
        for j in range(b_col_l):
            total = 0
            # iterate over columns in mat a, a_row column len == mat_b len
            for a_num, b_row in zip(a_row, m_b):
                b_num = b_row[j]
                validate_num_or_raise(a_num)
                validate_num_or_raise(b_num, "m_b")
                total += a_num * b_num
            new_matrix[i].append(total)
    return new_matrix
