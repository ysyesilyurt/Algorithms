#!/usr/bin/env python3

"""
Sample Input
2
hello
world
hi
world

Sample Output
YES
NO
"""


def twoStrings(lst):
    for strs in lst:
        letters = {}
        flag = True
        for letter in strs[0]:
            try:
                letters[letter] += 1
            except KeyError:
                letters[letter] = 1
        for letter in strs[1]:
            if letter in letters:
                print("YES")
                flag = False
                break
        if flag:
            print("NO")


if __name__ == '__main__':
    twoStrings([["hello", "world"], ["hi", "world"]])

