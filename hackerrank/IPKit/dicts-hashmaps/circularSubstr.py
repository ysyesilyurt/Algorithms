#!/usr/bin/env python3

"""
Problem
Given a target and source, return min length
anagram in give circular "source" string

Sample Input
kanah
hackerrank

Sample Output
5
"""


def circularSubstringCompetition(target, source):

    lens = len(source)
    lst = []
    dct = {}
    res = []
    for letter in target:
        try:
            dct[letter] += 1
        except KeyError:
            dct[letter] = 1
    for i in range(lens):
        if source[i] in dct:
            lst.append(i)
    lenl = len(lst)
    for i in range(lenl):
        x = 0
        dct2 = dict(dct)
        j = lst[i]
        flag = False
        while True:
            if j == lens:
                flag = True
                j = 0
            elif flag and j == lst[i]:
                break
            x += 1
            if source[j] in dct2:
                try:
                    dct2[source[j]] -= 1
                    if dct2[source[j]] == 0:
                        del dct2[source[j]]
                except KeyError:
                    continue
            if dct2 == {}:
                res.append(x)
                break
            j += 1
    if res == []:
        return -1
    else:
        return min(res)


if __name__ == '__main__':

    #res = circularSubstringCompetition("krr", "hackerrank")
    res = circularSubstringCompetition("kanah", "hackerrank")
    print(res)
