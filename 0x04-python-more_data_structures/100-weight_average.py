#!/usr/bin/python3


def weight_average(my_list=[]):
    """ Write a function that returns the weighted average of
    all integers tuple (<score>, <weight>) """
    if not my_list:
        return 0
    score_tot = 0
    weight_tot = 0
    for tup in my_list:
        score, weight = tup
        score_tot += score * weight
        weight_tot += weight
    return score_tot / weight_tot
