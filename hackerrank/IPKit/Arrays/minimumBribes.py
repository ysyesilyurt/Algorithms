#!/usr/bin/env python3

"""
Sample Input
2
8
5 1 2 3 7 8 6 4
8
1 2 5 3 7 8 6 4

Sample Output
Too chaotic
7
"""


def minimumBribes(q):

    # Bubble sort w/modifications
    # O(n^2) one is taking too long

    for queue in q:
        length = len(queue)
        bribeCount = 0
        chaotic = {}
        flag = False
        swapped = True
        while swapped:
            swapped = False
            for i in range(length-1):
                if queue[i] > queue[i+1]:
                    try:
                        chaotic[queue[i]] += 1
                        if chaotic[queue[i]] > 2:
                            print("Too chaotic")
                            flag = True
                            break
                    except KeyError:
                        chaotic[queue[i]] = 1
                    swapped = True
                    queue[i], queue[i+1] = queue[i+1], queue[i]
                    bribeCount += 1
            if flag:
                break
        if not flag:
            print(bribeCount)


if __name__ == '__main__':

    lst = []
    with open("inp.txt", "r") as inp:
        line = inp.readline()
        while line != "":
            lst.append(list(map(int, line.split(" "))))
            line = inp.readline()

    minimumBribes(lst)
