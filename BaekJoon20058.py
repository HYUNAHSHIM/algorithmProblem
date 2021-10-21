# BaekJoon20058.py
import copy
from collections import deque


n, Q = map(int, input().split())
N = 2 ** n
A = [[] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))
L = list(map(int, input().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def rotate(arr):
    new_arr = copy.deepcopy(arr)
    n = len(arr)

    for i in range(n):
        for j in range(n):
            arr[j][n - 1 - i] = new_arr[i][j]

    return arr


def reduce():
    global A, N, dx, dy

    new_arr = copy.deepcopy(A)
    for i in range(N):
        for j in range(N):
            if new_arr[i][j] <= 0:
                continue
            near = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    if new_arr[nx][ny] > 0:
                        near += 1
            if near < 3:
                A[i][j] -= 1


def print_result():
    global A, N

    sum_ice = 0
    for i in range(N):
        for j in range(N):
            sum_ice += A[i][j]
    print(sum_ice)

    # bfs
    visited = [[False for _ in range(N)] for _ in range(N)]
    group = 0
    groups = []

    for i in range(N):
        for j in range(N):
            # 이미 방문했거나 얼음이 없으면 continue
            if visited[i][j] or A[i][j] <= 0:
                continue
            queue = deque([[i, j, group]])
            group += 1
            visited[i][j] = True
            groups.append(1)

            while queue:
                value = queue.popleft()

                for k in range(4):
                    nx = value[0] + dx[k]
                    ny = value[1] + dy[k]

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if A[nx][ny] <= 0:
                        continue
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        groups[value[2]] += 1
                        queue.append([nx, ny, value[2]])
    groups.append(0)
    print(max(groups))


def solution():
    global N, Q, L, A

    for i in range(Q):
        # 부분 격자로 나눠서 시계 방향 90도 회전
        n = 2 ** L[i]  # 부분 격자 한변의 길이
        sub_num = N // n  # 한 변에 몇개의 부분 격자로 나뉘는지
        for j in range(sub_num):
            for k in range(sub_num):
                nx = 2 ** L[i] * j
                ny = 2 ** L[i] * k
                new_arr = rotate([[A[a][b] for b in range(ny, ny + n)] for a in range(nx, nx + n)])

                for a in range(n):
                    for b in range(n):
                        A[nx + a][ny + b] = new_arr[a][b]

        # 조건에 부합하는 칸의 얼음양 - 1
        reduce()

    # 1. 남아있는 얼음의 합 2. 가장 큰 덩어리가 차지하는 칸의 개수 프린트
    print_result()


solution()
