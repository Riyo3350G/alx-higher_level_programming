#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = set(my_list)
    adds = 0
    for i in unique:
        adds += i
    return adds
