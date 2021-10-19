# BaekJoon14503.py

answer = 0
N, M = map(int, input().split())
pos = [0, 0]
pos[0], pos[1], direction = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
is_all_clean = 0

# 현재 위치 청소
answer += 1
visited[pos[0]][pos[1]] = True

while True:
    # 왼쪽 방향이 아직 청소를 하지 않았고 벽도 아니라면
    left = [pos[0] + dx[(direction + 3) % 4], pos[1] + dy[(direction + 3) % 4]]
    if arr[left[0]][left[1]] == 0 and not visited[left[0]][left[1]]:
        direction = (direction + 3) % 4
        pos = left[:]
        # 현재 위치 청소
        answer += 1
        visited[pos[0]][pos[1]] = True
        is_all_clean = 0
        continue

    # 왼쪽 방향이 이미 청소를 했거나 벽이라면
    if is_all_clean < 3:
        direction = (direction + 3) % 4
        is_all_clean += 1
        continue
    else:
        # 4방향 모두 청소가 되어 있거나 벽인 경우
        direction = (direction + 3) % 4
        back = [0, 0]
        if direction == 0 or direction == 2:
            back = [pos[0] + dx[2 - direction], pos[1] + dy[2 - direction]]
        elif direction == 1 or direction == 3:
            back = [pos[0] + dx[4 - direction], pos[1] + dy[4 - direction]]
        # 뒤쪽 방향이 벽이라 후진을 할 수 없는 경우
        if arr[back[0]][back[1]] == 1:
            break
        else:
            pos = back[:]
            is_all_clean = 0


print(answer)
