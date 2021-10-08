# BaekJoon21609.py
from collections import deque
import copy


N, M = map(int, input().split())
result = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))


def gravity():
    global arr, N
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if arr[i][j] == -1 or arr[i][j] == -2:
                continue
            for k in range(i + 1, N):
                # 아래에 다른 블럭이 있을 경우
                if arr[k][j] != -2:
                    if i + 1 == k:
                        break
                    arr[k - 1][j] = arr[i][j]
                    arr[i][j] = -2
                    break
                # 마지막 칸인 경우
                if k >= N - 1:
                    arr[k][j] = arr[i][j]
                    arr[i][j] = -2
                    break


def solution():
    global N, arr, dx, dy, result

    while True:
        selected_group = []
        block_group = []  # 블록 그룹의 블록들 위치 좌표값 저장
        visited = [[False] * N for _ in range(N)]  # 방문 여부 저장

        for i in range(N):
            for j in range(N):
                # 무지개 블록의 방문 여부 초기화
                for k in range(N):
                    for t in range(N):
                        if arr[k][t] == 0:
                            visited[k][t] = False

                # 일반블록이 아니거나 방문한 곳이면 continue
                if arr[i][j] <= 0 or visited[i][j]:
                    continue
                queue = deque([[i, j]])
                visited[i][j] = True
                block_group.append([[i, j]])
                color = arr[i][j]

                # bfs
                while queue:
                    value = queue.popleft()

                    for k in range(4):
                        nx = value[0] + dx[k]
                        ny = value[1] + dy[k]

                        # 게임판 밖으로 넘어가면 continue
                        if nx >= N or ny >= N or nx < 0 or ny < 0:
                            continue
                        # 검은색 블록이거나 방문한 블록인 경우 continue
                        if arr[nx][ny] == -1 or arr[nx][ny] == -2 or visited[nx][ny]:
                            continue
                        # 다른색 일반블록인 경우 continue:
                        if arr[nx][ny] > 0 and arr[nx][ny] != color:
                            continue

                        block_group[-1].append([nx, ny])
                        queue.append([nx, ny])
                        visited[nx][ny] = True

        # 가장 큰 블록 그룹 구하기
        block_max = []
        for group in block_group:
            length = len(group)
            # 블록 그룹 크기가 2 미만이면 블록 그룹 성립X
            if length < 2:
                continue
            # 크기 비교 후, 큰 그룹 선택
            if len(block_max) == 0:
                block_max.append(copy.deepcopy(group))
                continue
            if len(block_max[0]) < length:
                block_max = [copy.deepcopy(group)]
            elif len(block_max[0]) == length:
                block_max.append(copy.deepcopy(group))

        # 블록 그룹이 존재하지 않는 경우
        if len(block_max) == 0:
            print(result)
            break

        # 크기가 큰 블록이 하나면 해당 그룹 선택
        if len(block_max) == 1:
            selected_group = copy.deepcopy(block_max[0])
        else:
            # 크기가 큰 블록이 둘 이상이면 무지개 블록 수로 그룹 선택
            rainbow_blocks = []
            for group in block_max:
                rainbow_block = 0
                for block in group:
                    if arr[block[0]][block[1]] == 0:
                        rainbow_block += 1
                rainbow_blocks.append(rainbow_block)
            rainbow_max = rainbow_blocks.count(max(rainbow_blocks))

            # 무지개 블록 개수가 최대인 그룹이 하나면 해당 그룹 선택
            if rainbow_max == 1:
                selected_group = copy.deepcopy(block_max[rainbow_blocks.index(max(rainbow_blocks))])
            else:
                # 최대인 그룹이 둘 이상이면 기준 블록 구해서 행 크기로 선택
                block_max = [block_max[i] for i in range(len(rainbow_blocks)) if rainbow_blocks[i] == max(rainbow_blocks)]
                rep_blocks = []
                for group in block_max:
                    group.sort(key=lambda x: (x[0], x[1]))
                    for block in group:
                        # 무지개 블록이 아닌 기준 블록
                        if arr[block[0]][block[1]] != 0:
                            rep_blocks.append(copy.deepcopy(block))
                            break
                rep_blocks.sort(key=lambda x: (x[0], x[1]))
                for group in block_max:
                    if rep_blocks[-1] in group:
                        selected_group = copy.deepcopy(group)

        # selected_group 제거
        for block in selected_group:
            arr[block[0]][block[1]] = -2

        # 점수 획득
        result += len(selected_group) ** 2

        # 중력 작용
        gravity()

        # 90도 반시계 회전
        new_arr = copy.deepcopy(arr)
        for i in range(N):
            for j in range(N):
                arr[i][j] = new_arr[j][N - i - 1]

        # 중력 작용
        gravity()


solution()
