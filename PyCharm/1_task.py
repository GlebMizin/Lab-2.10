#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def geometric_mean(*a):
    if a:
        count = 0
        k = 1
        for num in a:
            k *= num
            count += 1
        return math.pow(k, 1/count)
    else:
        return "None"


print(f'Geometric mean of entered args: {geometric_mean(2,5,6,8)}')
