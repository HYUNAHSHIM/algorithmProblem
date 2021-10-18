# BaekJoon14499.py

N, M, x, y, k = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
operations = list(map(int, input().split()))
dice = [i for i in range(6)]
dice_num = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}


def move(di):
    global N, M, x, y, board
    rotate = [[2, 5, 3, 0], [3, 5, 2, 0], [1, 5, 4, 0], [4, 5, 1, 0]]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    # di 동0 서1 북2 남3
    nx = x + dx[di]
    ny = y + dy[di]
    # 보드 밖으로 나가는 경우
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return -1
    # 주사위 이동
    first = dice[rotate[di][0]]
    dice[rotate[di][0]] = dice[rotate[di][3]]
    dice[rotate[di][3]] = dice[rotate[di][2]]
    dice[rotate[di][2]] = dice[rotate[di][1]]
    dice[rotate[di][1]] = first
    # 숫자 update
    if board[nx][ny] == 0:
        board[nx][ny] = dice_num[dice[5]]
    else:
        dice_num[dice[5]] = board[nx][ny]
        board[nx][ny] = 0
    # x, y 업데이트
    x = nx
    y = ny

    return dice_num[dice[0]]


def solution():
    global N, M, x, y, k

    for op in operations:
        up = move(op - 1)

        if up == -1:
            continue
        else:
            print(up)


solution()
