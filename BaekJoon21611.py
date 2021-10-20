# BaekJoon21611.py

N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
d = [0 for _ in range(M)]
s = [0 for _ in range(M)]
for i in range(M):
    d[i], s[i] = map(int, input().split())
exploded = [0, 0, 0]
shark = [(N - 1) // 2, (N - 1) // 2]


# 블리자드로 구슬 파괴
def blizard(d, s):
    global shark, board, N

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(1, s + 1):
        nx = shark[0] + dx[d] * i
        ny = shark[1] + dy[d] * i

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        board[nx][ny] = 0


# board를 순서대로 arr로 반환
def get_the_list():
    global N, shark, board

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cur = shark[:]
    direction = 0
    num = 1
    arr = []

    is_over = False
    while not is_over:
        for i in range(2):
            for j in range(num):
                cur[0] += dx[direction]
                cur[1] += dy[direction]

                if cur[0] < 0 or cur[1] < 0 or cur[0] >= N or cur[1] >= N:
                    is_over = True
                    break
                arr.append(board[cur[0]][cur[1]])
            if is_over:
                break
            direction = (direction + 1) % 4
        num += 1

    return arr


def remove_zero(arr):
    new_arr = []
    for i in arr:
        if i != 0:
            new_arr.append(i)

    return new_arr


def explode(arr):
    global exploded

    is_removed = False
    marble_num = 1
    selected_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == selected_num:
            marble_num += 1
        else:
            # 연속하는 구슬이 4개 이상인 경우
            if marble_num >= 4:
                for j in range(1, marble_num + 1):
                    arr[i - j] = 0
                    is_removed = True
                exploded[selected_num - 1] += marble_num
            marble_num = 1
            selected_num = arr[i]
    if marble_num >= 4:
        for j in range(1, marble_num + 1):
            arr[len(arr) - 1 - j] = 0
            is_removed = True
        exploded[selected_num - 1] += marble_num

    return arr, is_removed


def change_group(arr):
    if not arr:
        return []

    new_arr = []
    marble_num = 1
    selected_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == selected_num:
            marble_num += 1
        else:
            new_arr.append(marble_num)
            new_arr.append(selected_num)
            marble_num = 1
            selected_num = arr[i]
    new_arr.append(marble_num)
    new_arr.append(selected_num)

    return new_arr


def rebuild_board(arr):
    global N, shark

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cur = shark[:]
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    direction = 0
    num = 1
    arr_num = 0

    if not arr:
        return new_board

    is_over = False
    while not is_over:
        for i in range(2):
            for j in range(num):
                cur[0] += dx[direction]
                cur[1] += dy[direction]

                if cur[0] < 0 or cur[1] < 0 or cur[0] >= N or cur[1] >= N:
                    is_over = True
                    break

                if arr_num >= len(arr):
                    is_over = True
                    break
                new_board[cur[0]][cur[1]] = arr[arr_num]
                arr_num += 1
            if is_over:
                break
            direction = (direction + 1) % 4
        num += 1

    return new_board


def solution():
    global M, d, s, board

    for i in range(M):
        blizard(d[i] - 1, s[i])
        arr = get_the_list()
        arr = remove_zero(arr)
        while arr:
            arr, is_removed = explode(arr)
            if not is_removed:
                break
            arr = remove_zero(arr)
        arr = change_group(arr)
        board = rebuild_board(arr)

    print(exploded[0] + 2 * exploded[1] + 3 * exploded[2])


solution()
