#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def average_harm(*a):
    if a:
        k = 0
        count = 0
        for num in a:
            k += 1/num
            count += 1
        return count/k
    else:
        return "None"


print(f'Average of entered args: {average_harm(5, 2, 3)}')
