# BaekJoon1182.py

N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * N
result = 0


def check_false():
    global visited
    for i in range(N):
        if visited[i]:
            return True
    return False


def solve(summ, start):
    global result, N, S
    if summ == S and check_false():
        result += 1
    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            summ += arr[i]
            solve(summ, i)
            visited[i] = False
            summ -= arr[i]


solve(0, 0)
print(result)
