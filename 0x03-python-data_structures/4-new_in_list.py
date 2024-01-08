#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    len_of_list = len(my_list)
    if idx < 0 or idx > len_of_list - 1:
        return my_list

    new_list[idx] = element
    return new_list
