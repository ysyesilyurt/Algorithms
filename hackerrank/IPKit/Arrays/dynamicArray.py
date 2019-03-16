#!/usr/bin/env python3

"""
Sample Input
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

Sample Output
7
3
"""


class QueryException(Exception):
    pass


def dynamicArray(n, queries):

    # O(querySize)

    lastAnswer = 0
    seqList = [[] for _ in range(n)]

    for query in queries:
        if query[0] == 1:
            seqList[(query[1] ^ lastAnswer) % n].append(query[2])
        elif query[0] == 2:
            lastAnswer = seqList[(query[1] ^ lastAnswer) % n][query[2] % len(seqList[(query[1] ^ lastAnswer) % n])]
            print(lastAnswer)
        else:
            raise QueryException("A Query of type 1 or 2 needs to be given!")


if __name__ == '__main__':
    queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    dynamicArray(2, queries)
