# BaekJoon20057.py

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
result = 0


def spread(x, y, d):
    global arr, dx, dy, N, result

    amount = arr[x][y]
    arr[x][y] = 0
    alpa = amount
    percent = [1, 2, 7, 10, 5]
    direction = [[[-1, -2], [1, -2]], [[1, 1], [-1, -1]], [[1], [-1]], [[0, 1], [0, -1]], [[0, 0]]]

    for i in range(5):
        spreaded = amount * percent[i] // 100
        direction_i = direction[i]
        for j in direction_i:
            nx = x
            ny = y
            for k in j:
                nx += dx[(d + k) % 4]
                ny += dy[(d + k) % 4]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                result += spreaded
                alpa -= spreaded
            else:
                arr[nx][ny] += spreaded
                alpa -= spreaded

    # 알파
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        result += alpa
    else:
        arr[nx][ny] += alpa


def solution():
    global arr, dx, dy, N

    direction = 0
    num = 1
    cur = [(N - 1) // 2, (N - 1) // 2]
    is_over = False

    while not is_over:
        for i in range(2):
            for j in range(num):
                cur[0] += dx[direction]
                cur[1] += dy[direction]

                if cur[0] < 0 or cur[1] < 0 or cur[0] >= N or cur[1] >= N:
                    is_over = True
                    break
                spread(cur[0], cur[1], direction)
            direction = (direction + 1) % 4
            if is_over:
                break
        num += 1

    print(result)


solution()
