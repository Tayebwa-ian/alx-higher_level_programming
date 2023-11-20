#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print(my_list[i], end="")
                n += 1
            else:
                continue
        print()
    except IndexError as er:
        raise er
    return n


if __name__ == "__main__":
    safe_print_list_integers()
