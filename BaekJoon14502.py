# BaekJoon14502.py
from itertools import combinations
from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
empty_block = []
virus_block = []
wall_num = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        arr[i][j] = tmp[j]
        if tmp[j] == 0:
            empty_block.append([i, j])
        elif tmp[j] == 1:
            wall_num += 1
        elif tmp[j] == 2:
            virus_block.append([i, j])


# 안전영역의 크기 구하기
def bfs():
    global arr, virus_block, N, M, wall_num, dx, dy

    non_safe_zone = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for virus in virus_block:
        if visited[virus[0]][virus[1]]:
            continue
        queue = deque([[virus[0], virus[1]]])
        visited[virus[0]][virus[1]] = True

        while queue:
            value = queue.popleft()

            for i in range(4):
                nx = value[0] + dx[i]
                ny = value[1] + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if not visited[nx][ny] and arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    non_safe_zone += 1
                    queue.append([nx, ny])

    return N * M - (wall_num + 3) - non_safe_zone - len(virus_block)


def solution():
    global empty_block, arr

    answer = 0
    combis = list(combinations(empty_block, 3))
    for combi in combis:
        # 지도에 3개의 벽 세우기
        for x, y in combi:
            arr[x][y] = 1

        # bfs로 안전 영역의 크기 구하기
        safe_zone = bfs()
        answer = max(answer, safe_zone)

        # 지도 원상복귀
        for x, y in combi:
            arr[x][y] = 0

    return answer


print(solution())
