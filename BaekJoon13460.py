# BaekJoon13460.py
from collections import deque


N, M = map(int, input().split())
R = [0, 0]
B = [0, 0]
hole = [0, 0]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    tmp = list(input())
    for j in range(M):
        board[i][j] = tmp[j]
        if tmp[j] == 'R':
            R = [i, j]
            board[i][j] = "."
        elif tmp[j] == 'B':
            B = [i, j]
            board[i][j] = "."
        elif tmp[j] == 'O':
            hole = [i, j]


# direction으로 빨간 구슬과 파란 구슬 옮기고 각자 위치 반환
def move(r, b, direction):
    global hole, board

    red = r[0] * direction[0] + r[1] * direction[1]
    blue = b[0] * direction[0] + b[1] * direction[1]
    marbles = []
    is_finished = [False, False]

    # 빨간 구슬이 파란 구슬보다 앞에 있다면
    if red >= blue:
        marbles.append(r)
        marbles.append(b)
    else:
        marbles.append(b)
        marbles.append(r)
    # 순서대로 이동
    while True:
        for i in range(2):
            if is_finished[i]:
                continue
            tr = [marbles[i][0] + direction[0], marbles[i][1] + direction[1]]
            # 구멍이 있으면 -1
            if tr == hole:
                marbles[i] = [-1, -1]
                is_finished[i] = True
            # 벽이거나 다른 구슬이 있으면 멈춤
            elif board[tr[0]][tr[1]] == "#" or tr == marbles[1 - i]:
                is_finished[i] = True
            # 아무것도 없으면 계속 한칸씩 이동
            else:
                marbles[i] = [tr[0], tr[1]]
        # 두 구슬 다 움직일 수 없다면 종료
        if is_finished[0] and is_finished[1]:
            break

    if red >= blue:
        return marbles
    else:
        return [marbles[1], marbles[0]]


def bfs():
    global N, M, board, R, B, dx, dy

    queue = deque([[R, B, 0]])  # 빨간 구슬 위치, 파란 구슬 위치, 움직인 횟수

    while queue:
        r, b, n = queue.popleft()

        # 10번 넘으면 제외
        if n >= 10:
            continue

        # 4방향으로 이동
        for i in range(4):
            nr, nb = move(r, b, [dx[i], dy[i]])
            # 더이상 구슬이 움직이지 않으면 continue
            if r == nr and b == nb:
                continue
            # 파란 구슬이 구멍에 빠지면 continue
            if nb[0] == -1:
                continue
            # 빨간 구슬만 구멍에 빠지면 정답
            elif nr[0] == -1:
                return n + 1
            # 어느 구슬도 구멍에 빠지지 않으면 append
            else:
                queue.append([nr, nb, n + 1])

    return -1



print(bfs())
