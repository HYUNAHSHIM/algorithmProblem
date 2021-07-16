# BaekJoon2606.py
from collections import deque


def solution(N, M):
    link = [[] for _ in range(N)]
    visited = [False for _ in range(N)]

    for i in range(M):
        a, b = map(int, input().split())
        link[a - 1].append(b - 1)
        link[b - 1].append(a - 1)

    qu = deque([0])
    visited[0] = True
    answer = 0

    while len(qu) != 0:
        value = qu.popleft()
        for i in link[value]:
            if not visited[i]:
                answer += 1
                visited[i] = True
                qu.append(i)

    return answer


N = int(input())
M = int(input())
print(solution(N, M))
