#!/usr/bin/env python3

from collections import OrderedDict

"""
Sample Input
5 3
1 2 100
2 5 100
3 4 100

Sample Output
200
"""


def arrayManipulation(n, queries):

    # O(M) (M is query #)

    """
    Explanation -- At each iteration, We only add query[2] only the start of the range
                   and beyond the end of the range is decreased by query[2] amount.
                   i.e. if query = [1,2,100], then we would've [100,0,-100,0,0]

    Logic behind that is simple -- Differences of sums between the current range and the previous range
                                   are stored and every range is greater (or smaller if the value is
                                   negative) than its previous range with an amount of difference value.
    """
    maxNum = 0
    temp = 0
    nums = {}
    for query in queries:
        try:
            nums[query[0]-1] += query[2]
        except KeyError:
            nums[query[0]-1] = query[2]
        try:
            nums[query[1]] -= query[2]
        except KeyError:
            nums[query[1]] = -query[2]

    rnges = OrderedDict(sorted(nums.items(), key=lambda t: t[0]))
    for rnge in rnges:
        temp += rnges[rnge]
        if temp > maxNum:
            maxNum = temp
    return maxNum


if __name__ == '__main__':

    """
    queries = [[1,2,100], [2,5,100], [3,4,100]]
    res = arrayManipulation(10, queries)
    print(res)
    """
    lst = []
    with open("inp.txt", "r") as inp:
        line = inp.readline()
        while line != "":
            lst.append(list(map(int, line.split(" "))))
            line = inp.readline()
    res = arrayManipulation(10000000, lst)
    print(res)

