#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            n += 1
        print()
    except (TypeError, ValueError):
        pass
    return n


if __name__ == "__main__":
    safe_print_list_integers()
