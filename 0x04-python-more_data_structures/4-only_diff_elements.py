#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2

''' OR
def only_diff_elements(set_1, set_2):
    common = set_1 & set_2
    combined = []
    union = []
    for elem in set_1:
        combined.append(elem)
    for elem in set_2:
        combined.append(elem)
    for elem in combined:
        if elem not in common:
            union.append(elem)
    return sorted(union)
    ''' 
