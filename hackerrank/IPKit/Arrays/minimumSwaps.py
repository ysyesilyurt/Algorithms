#!/usr/bin/env python3

"""
Sample Input
7
1 3 5 2 4 6 7

Sample Output
3
"""


def minimumSwaps(arr):

    # O(n)

    swaps = 0
    length = len(arr)
    i = 0
    while i < length:
        if arr[i] != i+1:
            temp = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = temp
            swaps += 1
        else:
            i += 1
    return swaps


if __name__ == '__main__':

    with open("inp.txt", "r") as inp:
        line = inp.readline()
        lst = list(map(int, line.split(" ")))
        res = minimumSwaps(lst)
        print(res)
