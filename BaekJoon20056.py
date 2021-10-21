# BaekJoon20056.py
import copy


N, M, K = map(int, input().split())
fireball = {}
fireball_n = 0
for i in range(M):
    fireball[i] = list(map(int, input().split()))
    fireball[i][0] -= 1
    fireball[i][1] -= 1
    fireball_n += 1
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


# 파이어볼 방향 d로 속력 s칸 만큼 이동
def move():
    global fireball, dx, dy, N
    for f in fireball.values():
        f[0] = (f[0] + dx[f[4]] * f[3] - N) % N
        f[1] = (f[1] + dy[f[4]] * f[3] - N) % N


def is_all_same(arr):
    is_odd = 0
    is_same = True
    for i in range(len(arr)):
        if i == 0:
            is_odd = arr[i] % 2
            continue
        if arr[i] % 2 != is_odd:
            is_same = False
    return is_same


# 2개 이상의 파이어볼이 있는 칸의 파이어볼 합체
def union():
    global fireball, N, fireball_n

    arr = [[[] for _ in range(N)] for _ in range(N)]
    for key in fireball.keys():
        arr[fireball[key][0]][fireball[key][1]].append(key)

    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) < 2:
                continue
            fs = arr[i][j]
            same = is_all_same([fireball[f][4] for f in fs])
            m, s = 0, 0
            for f in fs:
                m += fireball[f][2]
                s += fireball[f][3]
                del fireball[f]
            if m // 5 == 0:
                continue
            if same:
                di = [0, 2, 4, 6]
                for k in range(4):
                    fireball[fireball_n] = [i, j, m // 5, s // len(fs), di[k]]
                    fireball_n += 1
            else:
                di = [1, 3, 5, 7]
                for k in range(4):
                    fireball[fireball_n] = [i, j, m // 5, s // len(fs), di[k]]
                    fireball_n += 1


def print_result():
    global fireball

    result = 0
    for f in fireball.values():
        result += f[2]
    print(result)


def solution():
    global K, fireball

    for _ in range(K):
        move()
        union()
    print_result()


solution()
