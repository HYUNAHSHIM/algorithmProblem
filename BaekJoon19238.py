# BaekJoon19238.py
from collections import deque
import sys
input = sys.stdin.readline


N, M, energy = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
car = list(map(int, input().split()))
car[0] -= 1
car[1] -= 1
people = {}  # arr에 표시한 승객 번호를 key로, 출발지 & 목적지 좌표를 value로
for i in range(M):
    p = list(map(int, input().split()))
    for j in range(4):
        p[j] -= 1
    arr[p[0]][p[1]] = i + 2
    people[i + 2] = p
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 최단 거리가 가장 짧은 승객 선택 -> 행 번호 가장 작은 -> 열 번호 가장 작은
def select(x, y):
    global arr, people, M, dx, dy

    visited = [[False for _ in range(N)] for _ in range(N)]
    selected = 0
    distance = float('inf')
    queue = deque([[x, y, 0]])  # x, y좌표, 차로부터의 거리
    visited[x][y] = True
    while queue:
        v = queue.popleft()
        # 해당 위치에 승객이 있다면
        if arr[v[0]][v[1]] != 0 and arr[v[0]][v[1]] != 1:
            if distance < v[2]:  # 이미 최단 거리가 아니므로 bfs 종료
                break
            elif distance > v[2]:  # 최단 거리인 승객 update
                selected = arr[v[0]][v[1]]
                distance = v[2]
            elif distance == v[2]:  # 행, 열 더 작은 승객 선택
                tmp = sorted([[people[selected][0], people[selected][1]], [v[0], v[1]]], key=lambda x: (x[0], x[1]))[0]
                selected = arr[tmp[0]][tmp[1]]
        else:
            for i in range(4):
                nx = v[0] + dx[i]
                ny = v[1] + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if not visited[nx][ny] and arr[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append([nx, ny, v[2] + 1])
    return selected, distance


# p 위치로 이동 후 p 승객의 목적지로 이동
def move(p, d):
    global car, arr, energy, people, N, dx, dy

    # p 승객의 출발지로 이동
    # 연료가 부족하면 종료
    if d >= energy:
        return False
    car = [people[p][0], people[p][1]]
    energy -= d

    # bfs로 승객의 목적지까지 최단 거리 구해서 이동
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque([[car[0], car[1], 0]])
    visited[car[0]][car[1]] = True
    while queue:
        v = queue.popleft()
        if v[0] == people[p][2] and v[1] == people[p][3]:  # 승객의 목적지에 도착했다면
            # 연료 체크
            if v[2] > energy:
                return False
            car = [v[0], v[1]]
            energy = energy + v[2]
            # 승객 도착했으므로 지우기
            arr[people[p][0]][people[p][1]] = 0
            del people[p]
            return True
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny] and arr[nx][ny] != 1:
                queue.append([nx, ny, v[2] + 1])
                visited[nx][ny] = True

    return False


def solution():
    global M, car, energy

    for i in range(M):
        p, d = select(car[0], car[1])
        if not move(p, d):
            print(-1)
            return
    print(energy)
    return


solution()
