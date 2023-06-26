#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for sup in range(1, 3):
        try:
            if sup > a:
                raise Exception('Too far')
            else:
                result += a ** b / sup
        except Exception:
            result = b + a
            break
    return result
