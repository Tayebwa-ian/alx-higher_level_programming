#!/usr/bin/python3
import hidden_4


def main():
    lis = dir(hidden_4)
    for i in range(len(lis)):
        if(lis[i][0] != '_'):
            print("{}".format(lis[i]))


if __name__ == "__main__":
    main()
