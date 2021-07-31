# BaekJoon9019.py
from collections import deque
import sys


def solution():
    visited = [False for _ in range(10000)]
    queue = deque([[a, ""]])
    visited[a] = True

    while len(queue) != 0:
        value = queue.popleft()
        if value[0] == b:
            return value[1]

        # D
        next_value = (2 * value[0]) % 10000
        if not visited[next_value]:
            queue.append([next_value, value[1] + "D"])
            visited[next_value] = True
        # S
        if value[0] == 0:
            if not visited[9999]:
                queue.append([9999, value[1] + "S"])
                visited[9999] = True
        else:
            next_value = value[0] - 1
            if not visited[next_value]:
                queue.append([next_value, value[1] + "S"])
                visited[next_value] = True
        # L
        next_value = (value[0] % 1000) * 10 + int(value[0] / 1000)
        if not visited[next_value]:
            queue.append([next_value, value[1] + "L"])
            visited[next_value] = True
        # R
        next_value = int(value[0] / 10) + (value[0] % 10) * 1000
        if not visited[next_value]:
            queue.append([next_value, value[1] + "R"])
            visited[next_value] = True


input = sys.stdin.readline
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(solution())
