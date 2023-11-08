#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    deno = 0
    if len(my_list) != 0:
        for i in my_list:
            num += i[0] * i[1]
            deno += i[1]
            result = num/deno
        return result
    else:
        return 0
