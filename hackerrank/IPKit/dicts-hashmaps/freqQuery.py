#!/usr/bin/env python3

from collections import Counter

"""
Sample Input
4
3 4
2 1003
1 16
3 1
Sample Output
0
1
"""


class QueryException(Exception):
    pass


def freqQuery(queries):
    res = []
    dct = Counter()
    freqDct = Counter()
    for q in queries:
        if q[0] == 1:
            dct[q[1]] += 1
            freqDct[dct[q[1]]] += 1
            freqDct[dct[q[1]]-1] -= 1
            if freqDct[dct[q[1]]-1] <= 0:
                del freqDct[dct[q[1]]-1]
        elif q[0] == 2:
            dct[q[1]] -= 1
            freqDct[dct[q[1]] + 1] -= 1
            if freqDct[dct[q[1]] + 1] <= 0:
                del freqDct[dct[q[1]] + 1]
            if dct[q[1]] <= 0:
                del dct[q[1]]
            if q[1] in dct:
                freqDct[dct[q[1]]] += 1
        elif q[0] == 3:
            if q[1] in freqDct:
                res.append(1)
            else:
                res.append(0)
        else:
            raise QueryException("A query of type 1,2 or 3 needs to be given")
    return res


if __name__ == '__main__':
    #res = freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]])
    #print(res)
    lst = []
    with open("inp.txt", "r") as inp:
        line = inp.readline().rstrip().split(" ")
        while line != [""]:
            lst.append(list(map(int, line)))
            line = inp.readline().rstrip().split(" ")
        res = freqQuery(lst)
    with open("out.txt", "w") as out:
        for i in res:
            out.write(str(i) + '\n')

