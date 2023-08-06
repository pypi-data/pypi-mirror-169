#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random


def get_gauss_random_num(min_value, max_value):
    """
        按照高斯分布取随机值
    """
    mu = (min_value + max_value) / 2
    sigma = (max_value - mu) / 3
    s = random.gauss(mu, sigma)
    value = int(s)
    if value < min_value:
        return min_value
    if max_value > max_value:
        return max_value

    return value

