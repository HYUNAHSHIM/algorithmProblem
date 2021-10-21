# BaekJoon16235.py
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[5 for _ in range(N)] for _ in range(N)]
A = [[] for _ in range(N)]
for i in range(N):
    A[i] = list(map(int, input().split()))
trees = [[[] for _ in range(N)] for _ in range(N)]  # 나무의 위치 x, y, 나무의 나이
for i in range(M):
    tmp = list(map(int, input().split()))
    trees[tmp[0] - 1][tmp[1] - 1].append(tmp[2])


# 나이만큼 땅에서 양분을 먹고(어린 나무부터) 나이 + 1, 양분이 부족하면 죽어서 양분이 됨
def spring2summer():
    global arr, trees, N

    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if arr[i][j] < trees[i][j][k]:
                    dead = trees[i][j][k:]
                    trees[i][j] = trees[i][j][:k]
                    for tree in dead:
                        arr[i][j] += tree // 2
                    break
                arr[i][j] -= trees[i][j][k]
                trees[i][j][k] += 1


# 나이가 5의 배수인 나무가 번식에서 인접한 8개의 칸에 나이가 1인 나무가 생김
def fall():
    global trees, N

    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(N):
        for j in range(N):
            over_five = 0
            for tree in trees[i][j]:
                if tree % 5 == 0:
                    over_five += 1
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                trees[nx][ny] = [1 for _ in range(over_five)] + trees[nx][ny]


# A[r][c]만큼 땅에 양분이 추가됨
def winter():
    global A, arr, N

    for i in range(N):
        for j in range(N):
            arr[i][j] += A[i][j]


def solution():
    global K, trees, N

    for _ in range(K):
        spring2summer()
        fall()
        winter()

    result = 0
    for i in range(N):
        for j in range(N):
            result += len(trees[i][j])
    print(result)


solution()
