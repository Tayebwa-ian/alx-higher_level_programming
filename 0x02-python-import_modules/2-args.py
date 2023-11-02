#!/usr/bin/python3
from sys import argv


def main():
    num = len(argv)
    if num == 1:
        print("{} arguments.".format(num-1))
    else:
        print("{} arguments:".format(num-1))
    for i in range(num):
        if i == 0:
            continue
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
