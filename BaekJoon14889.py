# BaekJoon14889.py

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
combi = []
result = float('inf')


def calculate(team):
    global arr, N, result
    another_team = list(set([i for i in range(N)]) - set(team))

    a_score = 0
    b_score = 0
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            a_score += arr[team[i]][team[j]]
            a_score += arr[team[j]][team[i]]
            b_score += arr[another_team[i]][another_team[j]]
            b_score += arr[another_team[j]][another_team[i]]

    result = min(result, abs(a_score - b_score))


def combination(chosen):
    global N, arr

    if len(chosen) == N // 2:
        calculate(chosen)
        return

    last_chosen = chosen[-1] + 1 if chosen else 0
    for i in range(last_chosen, N):
        combination(chosen + [i])


combination([])
print(result)
