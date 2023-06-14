#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight = 0
    score = 0
    for k in my_list:
        score += k[0] * k[1]
        weight += k[1]
    return (score / weight)
