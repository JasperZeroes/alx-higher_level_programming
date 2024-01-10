#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy.append(replace)
        else:
            copy.append(my_list[i])
    return copy

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
search = 2
replace = 89
new_list = search_replace(my_list, search, replace)
print(new_list)
print(my_list)

''' OR
def search_replace(my_list, search, replace):
    new_list = []
    for num in my_list:
        if num == search:
            num = replace
            new_list.append(num)
        else:
            new_list.append(num)
    return new_list
    '''
