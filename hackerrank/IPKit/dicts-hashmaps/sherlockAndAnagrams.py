#!/usr/bin/env python3

import math

"""
Sample Input
2
ifailuhkqq
kkkk

Sample Output
3
10
"""


def sherlockAndAnagrams(strs):
    res = []
    for s in strs:
        count = 0
        lens = len(s)
        dct = {}
        for i in range(lens):
            for j in range(i, lens):
                x = "".join(sorted(s[i:j + 1]))
                try:
                    dct[x] += 1
                except KeyError:
                    dct[x] = 1
        for item in dct:
            if dct[item] > 1:
                dct[item] = int(math.factorial(dct[item]) / (math.factorial(dct[item] - 2) * 2))
                count += dct[item]
        res.append(count)
    return res


if __name__ == '__main__':
    res = sherlockAndAnagrams(["ifailuhkqq", "kkkk"])
    print(res)

