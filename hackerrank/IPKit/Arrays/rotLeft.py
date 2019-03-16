#!/usr/bin/env python3

"""
Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4
"""


def rotLeft(a, d):

    # O(n)

    length = len(a)
    arr = []
    for i in range(length):
        arr.append(a[(i+d) % length])
    for i in arr:
        print(i, end=" ")


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    rotLeft(arr, 4)
