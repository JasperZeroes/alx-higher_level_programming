#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv)
    counter = 0

    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("{} argument".format(count - 1))
        counter += 1
        print("{}: {}".format(counter, sys.argv[counter]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

        for i in range(1, len(sys.argv)):
            counter += 1
            print("{}: {}".format(counter, sys.argv[i]))
