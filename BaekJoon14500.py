# BaekJoon14500.py
from collections import deque
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[False for _ in range(M)] for _ in range(N)]
max_sum = -1


def dfs(x, y, num, summ):
    global N, M, arr, dx, dy, max_sum
    if num == 4:
        max_sum = max(max_sum, summ)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, num + 1, summ + arr[nx][ny])
            visited[nx][ny] = False


def solution():
    global N, M, arr, max_sum

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, arr[i][j])
            visited[i][j] = False
            # ㅓㅗㅜㅏ모양 검사
            # ㅏ
            if i < N - 2 and j < M - 1:
                max_sum = max(max_sum, arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j])
            # ㅜ
            if i < N - 1 and j < M - 2:
                max_sum = max(max_sum, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1])
            # ㅗ
            if i >= 1 and j < M - 2:
                max_sum = max(max_sum, arr[i][j] + arr[i-1][j+1] + arr[i][j+1] + arr[i][j+2])
            # ㅓ
            if 1 <= i < N - 1 and j < M - 1:
                max_sum = max(max_sum, arr[i][j] + arr[i-1][j+1] + arr[i][j+1] + arr[i+1][j+1])


solution()
print(max_sum)
