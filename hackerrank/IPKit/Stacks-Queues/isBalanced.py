#!/usr/bin/env python3

import os


def isBalanced(s):
    if len(s) % 2 != 0:
        return "NO"
    else:
        stack = []
        for letter in s:
            if stack == [] and (letter == '}' or letter == ')' or letter == ']'):
                return "NO"
            elif letter == '}':
                item = stack.pop()
                if item != '{':
                    return "NO"
            elif letter == ']':
                item = stack.pop()
                if item != '[':
                    return "NO"
            elif letter == ')':
                item = stack.pop()
                if item != '(':
                    return "NO"
            else:
                stack.append(letter)
        if stack != []:
            return "NO"
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
