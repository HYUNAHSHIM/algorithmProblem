# BaekJoon10159.py

N = int(input())
M = int(input())
relation = [[False for _ in range(N)] for _ in range(N)]

# 연결 배열 생성
for _ in range(M):
    a, b = map(int, input().split())
    relation[a - 1][b - 1] = 1

# 플로이드-와샬로 이동 가능한 보든 경로 구하기
for k in range(N):
    for i in range(N):
        for j in range(N):
            if relation[i][k] and relation[k][j]:
                relation[i][j] = True

# 출력
for i in range(N):
    cnt = 0
    for j in range(N):
        if not relation[i][j] and not relation[j][i]:
            cnt += 1
    print(cnt - 1)