#!/usr/bin/python3
def element_at(my_list, idx):
    len_of_list = len(my_list)
    if idx < 0 or idx > len_of_list - 1:
        return None
    for i in range(len_of_list):
        return my_list[idx]
