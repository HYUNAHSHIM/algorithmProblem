# Baekjoon16234.py
import sys


input = sys.stdin.readline
N, L, R = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
arr = [0 for _ in range(N)]
is_moved = True
result = 0

# 초기화
for i in range(N):
    arr[i] = list(map(int, input().split()))

while is_moved:
    is_moved = False
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group = []
                group_sum = 0
                stack = [[i, j]]
                visited[i][j] = True

                # dfs
                while stack:
                    top = stack.pop()
                    group.append([top[0], top[1]])
                    group_sum += arr[top[0]][top[1]]

                    for k in range(4):
                        for t in range(4):
                            x = top[0] + dx[k]
                            y = top[1] + dy[k]

                            if x < 0 or x >= N or y < 0 or y >= N:
                                continue
                            sub = abs(arr[x][y] - arr[top[0]][top[1]])
                            if L <= sub <= R and not visited[x][y]:
                                stack.append([x, y])
                                visited[x][y] = True
                                is_moved = True

                # 인구이동
                length = len(group)
                if length >= 2:
                    avg = group_sum // length
                    for k in range(length):
                        arr[group[k][0]][group[k][1]] = avg
    if is_moved:
        result += 1

print(result)
