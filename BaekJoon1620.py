# BaekJoon1620.py

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = ["" for _ in range(N)]
dic = {}

for i in range(N):
    arr[i] = input().rstrip()
    dic[arr[i]] = i + 1

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(arr[int(question) - 1])
    else:
        print(dic[question])
