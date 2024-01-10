#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    res = 0
    for i in new:
        res += i
    return res
'''
def uniq_add(my_list=[]):
    new_list = []
    result = 0

    for num in my_list:
    if num not in new_list:
        new_list.append(num)

    for num in new_list:
        result += num
    return result
'''
