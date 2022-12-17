#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def multiply_new(*args):
    if a:
        min_i = a.index(min(a)) + 1
        max_i = a.index(max(a))
        return math.prod(a[min_i:max_i])
    else:
        return None


if __name__ == "__main__":
    print(f'Multiply between min and max: {multiply_new(3,6,7,9)}')
