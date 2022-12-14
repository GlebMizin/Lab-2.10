#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def average_harm(*a):
    if a:
        nums = [1/num for num in a]
        out = len(nums)/math.fsum(nums)
        return out
    else:
        return "None"


print(f'Average of entered args: {average_harm(5, 2, 3)}')
