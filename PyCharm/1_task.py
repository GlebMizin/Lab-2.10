#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def geometric_mean(*a):
    if a:
        nums = [num for num in a]
        out = math.pow(math.prod(nums), 1/len(nums))
        return out
    else:
        return "None"


print(f'Geometric mean of entered args: {geometric_mean(2,5,6,8)}')
