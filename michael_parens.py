
# -*- coding=utf-8 -*-


def proper_parenthetics(string):
    """"""
    open_count = 0
    for paren in string:
        if paren == ')':
            open_count -= 1
        elif paren == '(':
            open_count += 1
        if open_count < 0:
            break
    if open_count < 0:
        return open_count
    elif open_count == 0:
        return open_count
    else:
        return 1
