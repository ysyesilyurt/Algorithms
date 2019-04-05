#!/usr/bin/env python3


def missingNumbers(arr, brr):
    arrDict = {}
    brrDict = {}
    missingItems = []

    for num in brr:
        try:
            brrDict[num] += 1
        except KeyError:
            brrDict[num] = 0

    for num in arr:
        try:
            arrDict[num] += 1
        except KeyError:
            arrDict[num] = 0

    for key in brrDict:
        if key not in arrDict:
            missingItems.append(key)
        elif brrDict[key] != arrDict[key]:
            missingItems.append(key)

    missingItems.sort()
    return missingItems


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print(" ".join(map(str, result)))
