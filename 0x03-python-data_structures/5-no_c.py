#!/usr/bin/python3
def no_c(my_string):
    without_cC = ""
    for i in range(len(my_string)):
        if my_string[i] not in 'cC':
            without_cC += my_string[i]
    return without_cC
