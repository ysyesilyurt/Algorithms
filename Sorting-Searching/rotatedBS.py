#!/usr/bin/env python3

"""
Sample Input
[5, 6, 7, 8, 9, 10, 1, 2, 3]
[3,56]

Sample Output
Found at index 8
Num is not in array
"""


def findPivot(arr):
    start = 0
    end = len(arr)
    mid = (start + end) // 2
    eternalEnd = len(arr)
    low = arr[start]
    high = arr[end-1]
    while start < end:
        if mid != eternalEnd and arr[mid] > arr[mid+1]:
            lst = arr[mid+1:] + arr[:mid+1]
            return [lst, len(arr[mid+1:])]
        if mid != 0 and arr[mid] < arr[mid-1]:
            lst = arr[mid:] + arr[:mid]
            return [lst, len(arr[mid:])]
        if arr[mid] > high:
            start = mid + 1
            mid = (start + end) // 2
        elif arr[mid] < low:
            end = mid - 1
            mid = (start + end) // 2


def rotatedBS(arr, rotFactor, nums):
    length = len(arr)
    for num in nums:
        start = 0
        end = length
        mid = (start + end) // 2
        while end >= start:
            if mid == length:
                print("Num is not in array")
                break
            if num > arr[mid]:
                start = mid + 1
                mid = (start + end) // 2
            elif num < arr[mid]:
                end = mid - 1
                mid = (start + end) // 2
            else:
                index = (mid-rotFactor) + length if (mid-rotFactor) < 0 else (mid-rotFactor)
                print("Found at index " + str(index))
                break
        else:
            print("Num is not in array")


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4]
    res = findPivot(arr)
    rotatedBS(res[0], res[1], [2, 56])

