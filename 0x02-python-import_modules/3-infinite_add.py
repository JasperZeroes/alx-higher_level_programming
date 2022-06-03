#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    result = 0

    '''if count == 1:
        print("{}".format(result))
    else:'''
    for i in range(1, count):
        result += int(sys.argv[i])
    print("{}".format(result))
