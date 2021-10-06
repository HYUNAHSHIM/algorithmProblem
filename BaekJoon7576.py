# BaekJoon7576.py
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tomato = []
visited = [[False for _ in range(M)] for _ in range(N)]
q = deque()
dx = [-1, 0, 1, 1]
dy = [1, -1, 1, 0]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append([i, j])


def solve():
    global M, N, arr, tomato, q, visited, dx, dy
    for i in range(len(tomato)):
        tomato[i].append(0)
        q.append(tomato[i])
        visited[tomato[i][0]][tomato[i][1]] = True
    value = []
    while q:
        value = q.popleft()
        for j in range(4):
            x = value[0] + dx[j]
            y = value[1] + dy[j]
            print(x, y, value[2])
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if not visited[x][y] and arr[x][y] == 0:
                q.append([x, y, value[2] + 1])
                visited[x][y] = True
                arr[x][y] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                print(-1)
                return
    print(value[2])
    return



solve()
