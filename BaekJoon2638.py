# BaekJoon2638.py
from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def check_cheeze_left():
    global arr
    for ls in arr:
        for l in ls:
            if l == 1:
                return True
    return False


def check_cheeze():
    global N, M, dx, dy, arr
    melting = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    queue = deque([[0, 0]])
    visited[0][0] = True
    while queue:
        value = queue.popleft()
        for i in range(4):
            nx = value[0] + dx[i]
            ny = value[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny] == 1:
                melting[nx][ny] += 1
                continue
            visited[nx][ny] = True
            queue.append([nx, ny])
    return melting


def delete_cheeze(cheezes):
    global arr, N, M
    for i in range(N):
        for j in range(M):
            if cheezes[i][j] >= 2:
                arr[i][j] = 0


def solution():
    result = 0
    while check_cheeze_left():
        delete_cheeze(check_cheeze())
        result += 1
    print(result)


solution()
