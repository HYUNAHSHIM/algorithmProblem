# BaekJoon14501.py

N = int(input())
T = [0 for _ in range(N)]
P = [0 for _ in range(N)]
for i in range(N):
    T[i], P[i] = map(int, input().split())
dp = [0 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    if N - i < T[i]:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

print(dp[0])
