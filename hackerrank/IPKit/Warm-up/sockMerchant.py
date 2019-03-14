#!/usr/bin/env python3

"""
Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output 
3
"""


def sockMerchant(n, ar):

    # O(n)

    socks = {}
    pairs = 0

    for i in ar:
        try:
            socks[str(i)] += 1
        except KeyError:
            socks[str(i)] = 1

    for i in socks:
        if socks[i] >= 2:
            while socks[i] > 1:
                pairs += 1
                socks[i] -= 2
    return pairs


if __name__ == '__main__':

    result = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    print(result)
