#!/usr/bin/env python3

import math

"""
Sample Input
6 3
1 3 9 9 27 81
Sample Output
6
"""

def countTriplets(arr, r):
    arr = sorted(arr)
    dct = {}
    count = 0
    for item in arr:
        if item == 1 or item % r == 0:
            try:
                dct[item] += 1
            except KeyError:
                dct[item] = 1
    i = arr[0]
    if arr[0] == arr[-1]:
        count = int(math.factorial(dct[i]) / (math.factorial(dct[i] - 3) * 6))
        return count
    elif r == 1:
        for num in dct:
            if dct[num] > 2:
                count += int(math.factorial(dct[num]) / (math.factorial(dct[num] - 3) * 6))
        return count
    while i < arr[-1]:
        try:
            count += dct[i] * dct[i * r] * dct[i * r * r]
            i *= r
        except KeyError:
            i *= r
    return count


if __name__ == '__main__':
    #res = countTriplets([1,3,9,9,27,81], 3)
    #print(res)
    with open("inp.txt", "r") as inp:
        line = list(map(int, inp.readline().split(" ")))
        res = countTriplets(line, 3)
        print(res)

