#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv)
    if count == 1:
        print("{} arguments.".format(count - 1))
    elif count == 2:
        print("{} argument:".format(count - 1))
        print("{}: {}".format(count - 1, argv[count - 1]))
    else:
        print("{} arguments:".format(count - 1))

        num = len(argv)
        if num == 1:
            print("{} arguments.".format(num - 1))
        elif num == 2:
            print("{} argument:".format(num - 1))
        else:
            print("{} arguments:".format(num - 1))

        for i in range(1, num):
            print("{}: {}".format(i, argv[i]))
