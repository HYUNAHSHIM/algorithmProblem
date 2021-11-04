# BaekJoon13913.py
from collections import deque


N, K = map(int, input().split())
visited = [False for _ in range(100001)]
before = [-1 for _ in range(100001)]  # 이동 경로 저장
queue = deque([[N, 0]])  # 수빈이 위치


def print_path(time):
    global before, K
    arr = []
    tmp = K
    for _ in range(time):
        arr.append(tmp)
        tmp = before[tmp]
    print(' '.join(map(str, arr[::-1])))


while queue:
    value = queue.popleft()

    # 수빈이가 동생과 만나는 경우
    if value[0] == K:
        print(value[1])
        print_path(value[1] + 1)
        break

    new = [value[0] - 1, value[0] + 1, value[0] * 2]
    for i in range(3):
        if new[i] < 0 or new[i] > 100000 or visited[new[i]]:
            continue
        visited[new[i]] = True
        queue.append([new[i], value[1] + 1])
        before[new[i]] = value[0]

