#!/usr/bin/python3
"""Minimum operations to get n characters"""


def factorize(num):
    div = 2
    factors = []
    while num > 1:
        if num % div == 0:
            factors.append(div)
            num /= div
        else:
            div += 1
    return factors


def minOperations(n):
    factors = factorize(n)
    clust = {}
    for factor in factors:
        clust[factor] = factors.count(factor)
    num_of_operations = 0
    for key, value in clust.items():
        num_of_operations += key*value
    return num_of_operations
