#!/usr/bin/python3

def search_replace(my_list, search, replace):
    rep_list = my_list[:]
    for i in range(len(rep_list)):
        if rep_list[i] == search:
            rep_list[i] = replace

    return rep_list
