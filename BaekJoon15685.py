# BaekJoon15685.py

N = int(input())
curve = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
arr = [[0 for _ in range(101)] for _ in range(101)]


def draw(c):
    curve = [c[2]]
    for i in range(c[3]):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)
    return curve


def make_dragon(x, y, c):
    global arr, dx, dy
    for i in range(len(c)):
        x += dx[c[i]]
        y += dy[c[i]]
        if x < 0 or y < 0 or x >= 101 or y >= 101:
            continue
        arr[x][y] = 1


def print_result():
    global arr
    result = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1 and arr[i + 1][j] == 1 and arr[i][j + 1] == 1 and arr[i + 1][j + 1] == 1:
                result += 1
    print(result)


def solution():
    global N, curve, arr

    for i in range(N):
        arr[curve[i][0]][curve[i][1]] = 1
        draw_curve = draw(curve[i])
        make_dragon(curve[i][0], curve[i][1], draw_curve)
    print_result()


solution()
