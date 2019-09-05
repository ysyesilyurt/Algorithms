#!/usr/bin/env python3

import math

"""
Sample Input
5 2
1 2 1 2 4
Sample Output
3
"""

def countTriplets(arr, r):
    numDct = {}
    res = 0
    if r == 1:
        for i in arr:
            try:
                numDct[i] += 1
            except KeyError:
                numDct[i] = 1
        for i in numDct:
            res += int((numDct[i] * (numDct[i]-1) * (numDct[i]-2)) / 6)
    else:
        duoDct = {}
        for i in arr:
            if i/r in numDct:
                try:
                    duoDct[(i / r, i)] += numDct[i/r]
                except KeyError:
                    duoDct[(i / r, i)] = numDct[i/r]
            if (i / r / r, i / r) in duoDct:
                res += duoDct[(i / r / r, i / r)]
            try:
                numDct[i] += 1
            except KeyError:
                numDct[i] = 1
    return res


if __name__ == '__main__':
    res = countTriplets([1,2,1,2,4], 2)
    print(res)
    # with open("inp.txt", "r") as inp:
    #     line = list(map(int, inp.readline().split(" ")))
    #     res = countTriplets(line, 3)
    #     print(res)

