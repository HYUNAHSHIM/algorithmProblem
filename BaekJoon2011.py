# BaekJoon2011.py
import sys
sys.setrecursionlimit(10000)


def solution(s):
    global mem

    length = len(s)

    if length == 0 or (length == 1 and int(s) != 0):
        return 1
    elif length in mem:
        return mem[length]
    else:
        if 10 <= int(s[-2:]) <= 26 and int(s[-1]) != 0:
            tmp = solution(s[:-1]) + solution(s[:-2])
        elif (10 > int(s[-2:]) or int(s[-2:]) > 26) and int(s[-1]) != 0:
            tmp = solution(s[:-1])
        elif 10 <= int(s[-2:]) <= 26 and int(s[-1]) == 0:
            tmp = solution(s[:-2])
        else:
            tmp = 0

        if length not in mem:
            mem[length] = tmp % 1000000

        return tmp % 1000000


secret = input()
mem = {}
if len(secret) == 0 or int(secret) == 0:
    print(0)
else:
    print(solution(secret))
