# BaekJoon20055.py

N, K = map(int, input().split())
A = list(map(int, input().split()))
result = 0
robots = [0 for _ in range(N)]


def rotate():
    global A, robots, N

    # 컨베이어 벨트 회전
    last = A.pop()
    A = [last] + A
    # 로봇 위치도 함께 변경
    robots.pop()
    robots = [0] + robots
    robots[-1] = 0


def move_robot():
    global robots, A

    for i in range(len(robots) - 1, 0, -1):
        if robots[i] == 0 and A[i] >= 1 and robots[i-1] != 0:
            robots[i] = 1
            A[i] -= 1
            robots[i-1] = 0


def add_robot():
    global robots, A

    if A[0] != 0:
        robots[0] += 1
        A[0] -= 1


def check():
    global A, K

    num = 0
    for i in A:
        if i == 0:
            num += 1
        if num >= K:
            return True


def solution():
    global result

    while True:
        result += 1
        rotate()
        move_robot()
        add_robot()
        if check():
            return result


print(solution())
