#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # unpack
    tup_a = (0, 0) if len(tuple_a) == 0 else tuple_a
    # accomodating for large tuple with *
    aa, ab, *_ = tup_a if len(tuple_a) > 1 else (tup_a[0], 0)
    tup_b = (0, 0) if len(tuple_b) == 0 else tuple_b
    ba, bb, *_ = tup_b if len(tuple_b) > 1 else (tup_b[0], 0)
    return (aa + ba, ab + bb)
