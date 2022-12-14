#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def multiply(*a):
    if a:
        min_ind = 0
        max_ind = 0
        min_values = min(a)
        max_values = max(a)

        for ind, val in enumerate(a):
            if val == min_values:
                min_ind = ind + 1
            elif val == max_values:
                max_ind = ind

        m = math.prod(a[min_ind:max_ind])
        return m
    else:
        return "None"


print(f'Multiply between min and max: {multiply(3,6,7,9)}')
