#!/usr/bin/python3

def best_score(a_dictionary):
    best_v = 0
    best_k = None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > best_v:
                best_v = v
                best_k = k
        return best_k
    else:
        return None
