#!/usr/bin/python3
from sys import argv


def main():
    num = len(argv)
    total = 0
    for i in range(num):
        if i == 0:
            continue
        total += int(argv[i])
    print("{}".format(total))


if __name__ == "__main__":
    main()
