#!/usr/bin/python3
import sys
def add(args):
    count = len(sys.argv)
    result = 0

    if count > 1:
        for i in range(1, count):
            result += int(sys.argv[i])
        return result
    else:
        return result

if (__name__ == '__main__'):
    print(add(sys.argv[1:]))
