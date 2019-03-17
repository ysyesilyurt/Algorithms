#!/usr/bin/env python3

"""
Sample Input
6 5
two times three is not four
two times two is four

Sample Output
No
"""


def checkMagazine(magazine, note):

    mag = {}
    for wrd in magazine:
        try:
            mag[wrd] += 1
        except KeyError:
            mag[wrd] = 1
    for wrd in note:
        try:
            mag[wrd] -= 1
            if mag[wrd] == 0:
                del mag[wrd]
        except KeyError:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':

    magazine = ["two", "times", "three", "is","not" ,"four"]
    checkMagazine(magazine, ["two", "times", "two", "is" ,"four"])

