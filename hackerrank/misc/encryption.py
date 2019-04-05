#!/usr/bin/env python3

import math


def encryption(s):
    grid = []
    index = 0
    row_number = math.floor(math.sqrt(len(s)))
    column_number = math.ceil(math.sqrt(len(s)))
    encoded_message = []
    merge_list = []

    if row_number * column_number < len(s):  # ensure that rows * columns >= L
        row_number += 1

    for i in range(row_number):  # parse the string into grid
        grid.append(s[:column_number])
        s = s[column_number:]

    for i in range(column_number):  # get the encoded message
        for j in grid:
            try:
                merge_list.append(j[index])
            except:
                continue
        merge_list = ''.join(merge_list)
        index += 1
        encoded_message.append(merge_list)
        merge_list = []

    return ' '.join(encoded_message)


if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
