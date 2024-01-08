#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = []

    if not my_list:
        return None

    max_num.append(my_list[0])

    for i in range(len(my_list)):
        if my_list[i] > max_num[0]:
            max_num[0] = my_list[i]
            # This will work too;  max_num.insert(0, my_list[i])
    return max_num[0]


'''def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    list_copy = my_list.copy()
    list_copy.sort()
    return list_copy[-1]   I love this version
'''
