#!/usr/bin/env python3

"""
Sample Input
0 0 1 0 0 1 0

Sample Output
4
"""


def jumpingOnClouds(c):

    # O(n)

    jumps = 0
    length = len(c)
    i = 0

    while i < length - 1:
        if i+2 < length:
            if c[i+2] != 1:
                i += 2
                jumps += 1
            else:
                i += 1
                jumps += 1
        else:
            i += 1
            jumps += 1

    return jumps


if __name__ == '__main__':

    result = jumpingOnClouds([0,0,1,0,0,1,0])
    print(result)
