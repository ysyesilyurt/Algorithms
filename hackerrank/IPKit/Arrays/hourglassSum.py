#!/usr/bin/env python3

"""
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19
"""


def hourglassSum(arr):

    # const
    
    sums = []
    accumulator = 0

    for i in range(16):
        accumulator += arr[0 + (i // 4)][0 + (i % 4)]
        accumulator += arr[0 + (i // 4)][1 + (i % 4)]
        accumulator += arr[0 + (i // 4)][2 + (i % 4)]
        accumulator += arr[1 + (i // 4)][1 + (i % 4)]
        accumulator += arr[2 + (i // 4)][0 + (i % 4)]
        accumulator += arr[2 + (i // 4)][1 + (i % 4)]
        accumulator += arr[2 + (i // 4)][2 + (i % 4)]
        sums.append(accumulator)
        accumulator = 0

    return max(sums)


if __name__ == '__main__':

    arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
    result = hourglassSum(arr)
    print(result)
