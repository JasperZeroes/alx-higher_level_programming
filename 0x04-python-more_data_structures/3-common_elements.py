#!/usr/bin/python3
def common_elements(set_1, set_2):
    return set(set_1) & set(set_2)

'''def common_elements(set_1, set_2):
    common = []
    for elem in set_1:
        if elem in set_2:
            common.append(elem)
    return common

print(common_elements(set_1, set_2))
'''
