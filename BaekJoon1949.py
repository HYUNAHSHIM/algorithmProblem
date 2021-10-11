# BaekJoon 1949.py
import sys

sys.setrecursionlimit(20000)
N = int(input())
people = [0] + list(map(int, input().split()))
visited = [False for _ in range(N + 1)]  # 방문여부 저장
s = [[] for _ in range(N + 1)]  # 연결리스트
dp = [[0] * 2 for _ in range(N + 1)]  # dp[n][1]: n번 마을을 우수마을로 선정했을 경우 우수 마을의 주민 수의 총합


def dfs(start):
    global visited, dp, people, s
    visited[start] = True
    dp[start][0] = people[start]  # start번을 우수마을로 선정했을 경우 주민 수 추가
    for i in s[start]:  # 연결된 모든 마을들에 대해서 rotate
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]  # 우수마을로 선정했을 경우 주변 마을은 우수마을로 선정x
            dp[start][1] += max(dp[i][0], dp[i][1])  # 우수마을로 선정하지 않았을 경우 주변 마을을 우수마을로 선정할지 결정


# 연결리스트 초기화
for _ in range(N - 1):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

dfs(1)
print(max(dp[1][0], dp[1][1]))
