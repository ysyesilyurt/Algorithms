#!/usr/bin/env python3

"""
Sample Input
8
UDDDUDUU

Sample Output
1

Explanation
_/\      _
   \    /
    \/\/
"""


def countingValleys(n, s):

    # O(n)

    seaLevel = 0
    valleyCount = 0

    for i in s:
        if i == 'U':
            seaLevel += 1
            if seaLevel == 0:
                valleyCount += 1
        elif i == 'D':
            seaLevel -= 1

    return valleyCount


if __name__ == '__main__':

    result = countingValleys(8, "UDDDUDUU")
    print(result)
