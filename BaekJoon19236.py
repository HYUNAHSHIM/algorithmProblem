# BaekJoon19236.py
import sys
input = sys.stdin.readline


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 초기 값인 경우
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] += dp[i][j - 1] if board[i][j] < board[i][j - 1] else dp[i][j - 1] + board[i][j] - board[i][j - 1] + 1
        elif j == 0:
            dp[i][j] += dp[i - 1][j] if board[i][j] < board[i - 1][j] else dp[i - 1][j] + board[i][j] - board[i - 1][j] + 1
        else:
            cost1 = dp[i][j - 1] if board[i][j] < board[i][j - 1] else dp[i][j - 1] + board[i][j] - board[i][j - 1] + 1
            cost2 = dp[i - 1][j] if board[i][j] < board[i - 1][j] else dp[i - 1][j] + board[i][j] - board[i - 1][j] + 1
            dp[i][j] = min(cost1, cost2)

print(dp[n - 1][n - 1])
