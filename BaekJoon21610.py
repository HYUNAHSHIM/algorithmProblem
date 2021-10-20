# BaekJoon21610.py

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
d = [0 for _ in range(M)]
s = [0 for _ in range(M)]
for i in range(M):
    d[i], s[i] = map(int, input().split())


def move_clouds(clouds, d, s, visited):
    global N, arr

    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for cloud in clouds:
        cloud[0] = cloud[0] + dx[d] * s
        cloud[1] = cloud[1] + dy[d] * s

        if cloud[0] < 0:
            if (-1 * cloud[0]) % N == 0:
                cloud[0] = 0
            else:
                cloud[0] = N - ((-1 * cloud[0]) % N)
        elif cloud[0] >= N:
            cloud[0] = cloud[0] % N
        if cloud[1] < 0:
            if (-1 * cloud[1]) % N == 0:
                cloud[1] = 0
            else:
                cloud[1] = N - ((-1 * cloud[1]) % N)
        elif cloud[1] >= N:
            cloud[1] = cloud[1] % N

        arr[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = True

    return clouds, visited


def magic(clouds):
    global arr

    dx = [-1, -1, 1, 1]
    dy = [-1, 1, 1, -1]

    for cloud in clouds:
        water_num = 0
        for i in range(4):
            nx = cloud[0] + dx[i]
            ny = cloud[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if arr[nx][ny] > 0:
                water_num += 1
        arr[cloud[0]][cloud[1]] += water_num


def make_clouds(clouds, visited):
    global arr, N

    new_clouds = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                new_clouds.append([i, j])
                arr[i][j] -= 2

    return new_clouds


def solution():
    global M

    clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]  # 초기 구름 위치
    for i in range(M):
        visited = [[False for _ in range(N)] for _ in range(N)]
        clouds, visited = move_clouds(clouds, d[i] - 1, s[i], visited)
        magic(clouds)
        clouds = make_clouds(clouds, visited)

    result = 0
    for i in range(N):
        for j in range(N):
            result += arr[i][j]
    print(result)


solution()
