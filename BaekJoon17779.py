# BaekJoon17779.py

answer = float('inf')
N = int(input())
A = [[] for _ in range(N)]
total = 0
for i in range(N):
    A[i] = list(map(int, input().split()))
    total += sum(A[i])


def divide(x, y, d1, d2):
    global N, A, total
    number = [0, 0, 0, 0, 0]
    divided = [[0 for _ in range(N)] for _ in range(N)]

    # 5번 구역 구하기

    # 5번 구역 경계선 표시
    for i in range(d1 + 1):
        divided[x + i][y - i] = 5
        divided[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        divided[x + i][y + i] = 5
        divided[x + d1 + i][y - d1 + i] = 5

    # 5번 구역 내부 표시하기
    for i in range(x + 1, x + d1 + d2):
        first_five = divided[i].index(5)
        second_five = first_five + divided[i][first_five + 1:].index(5) + 1

        for j in range(first_five, second_five + 1):
            divided[i][j] = 5

    # 나머지 구역 구하기
    for i in range(N):
        for j in range(N):
            if divided[i][j] == 5:
                continue
            if 0 <= i < x + d1 and 0 <= j <= y:
                number[0] += A[i][j]
            elif 0 <= i <= x + d2 and y < j < N:
                number[1] += A[i][j]
            elif x + d1 <= i < N and 0 <= j < y - d1 + d2:
                number[2] += A[i][j]
            elif x + d2 < i < N and y - d1 + d2 <= j < N:
                number[3] += A[i][j]

    number[4] = total - sum(number)
    return max(number) - min(number)


for x in range(1, N - 1):
    for y in range(1, N - 1):
        for d1 in range(1, y):
            for d2 in range(1, N - y):
                # 구역을 벗어나는 경우
                if d1 + d2 > N - 1 - x:
                    continue

                # 최소값 구하기
                answer = min(answer, divide(x, y, d1, d2))

print(answer)
