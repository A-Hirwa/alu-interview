#!/usr/bin/python3
"""Calculate the amount of rain that will be trapped after it rains
"""


def rain(walls):
    """Calculate the amount of rain that will be trapped after it rains
    """
    if not walls or len(walls) < 3:
        return 0
    results = 0
    for i in range(1, len(walls) - 1):
        max_left = max(walls[:i])
        max_right = max(walls[i + 1:])
        minlevel = min(max_left, max_right)
        if walls[i] < minlevel:
            results += minlevel - walls[i]
    return results
