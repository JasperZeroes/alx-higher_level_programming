#!/usr/bin/python3
for m in range(0, 9):
    for n in range(m + 1, 10):
        if m == 8 and n == 9:
            print("{}{}".format(m, n))
        else:
            if m != n:
                print("{}{}".format(m, n), end=", ")
