#!/usr/bin/env python3

"""
Sample Input
kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm
736778906400

Sample Output
51574523448
"""


def repeatedString(s, n):

    # O(n)

    initLen = len(s)
    count = 0

    for i in range(initLen):
        if s[i] == 'a':
            count += 1

    remainder = n % initLen
    multiplier = n//initLen
    count *= multiplier

    for i in range(remainder):
        if s[i] == 'a':
            count += 1

    return count


if __name__ == '__main__':

    result = repeatedString("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm", 736778906400)
    print(result)
