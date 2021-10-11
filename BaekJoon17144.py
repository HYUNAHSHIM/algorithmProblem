# BaekJoon17144.py
import copy


# 변수 및 배열 초기화
R, C, T = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
A = [[] for _ in range(R)]
cleaner = []
for i in range(R):
    A[i] = list(map(int, input().split()))

for _ in range(T):
    # 확산
    new_A = copy.deepcopy(A)
    for i in range(R):
        for j in range(C):
            # 공기 청정기 위치 저장
            if new_A[i][j] == -1:
                cleaner.append([i, j])
            # 미세먼지가 존재하는 경우
            if new_A[i][j] != -1 and new_A[i][j] != 0:
                # 확산된 방향 개수 저장용
                num = 0
                # 4방향 확산
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]

                    # 새로운 좌표가 배열에서 벗어나는 경우
                    if x < 0 or y < 0 or x >= R or y >= C:
                        continue
                    # 새로운 좌표의 위치에 공기청정기가 있는 경우
                    if new_A[x][y] == -1:
                        continue
                    # 확산량 계산
                    A[x][y] += new_A[i][j] // 5
                    num += 1
                A[i][j] -= (new_A[i][j] // 5) * num

    # 순환
    direction = [[[0, 1], [-1, 0], [0, -1], [1, 0]], [[0, 1], [1, 0], [0, -1], [-1, 0]]]
    for i in range(2):
        cur = copy.deepcopy(cleaner[i])
        cur[1] += 1
        dust = 0
        dir_num = 0
        while True:
            # 이전 미세먼지 이동
            new_dust = A[cur[0]][cur[1]]
            A[cur[0]][cur[1]] = dust
            dust = new_dust

            # 좌표 변경
            new_x = cur[0] + direction[i][dir_num][0]
            new_y = cur[1] + direction[i][dir_num][1]
            # 만약 방향 전환이 필요하다면
            if new_x < 0 or new_y < 0 or new_x >= R or new_y >= C:
                dir_num += 1
            cur[0] += direction[i][dir_num][0]
            cur[1] += direction[i][dir_num][1]
            if cur[0] == cleaner[i][0] and cur[1] == cleaner[i][1]:
                break

result = 0
for i in range(R):
    for j in range(C):
        if A[i][j] != -1:
            result += A[i][j]

print(result)
