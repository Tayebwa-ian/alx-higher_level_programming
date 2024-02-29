#!/usr/bin/python3
"""Find the peak value from a list"""


def find_peak(list_of_integers) -> int:
    """finds a peak in a list of unsorted integers
    Arg:
        list_of_integers: a list of unsorted integers
    Return: peak value or None
    """
    if len(list_of_integers) > 0:
        peak = list_of_integers[0]
        temp = list_of_integers[0]
        i = 0
        j = -1
        m = len(list_of_integers) // 2
        while i < m:
            temp = list_of_integers[i]
            if list_of_integers[i] < list_of_integers[j]:
                temp = list_of_integers[j]
            if temp > peak:
                peak = temp
            i += 1
            j -= 1
        return(peak)
