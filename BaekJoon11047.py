# BaekJoon11047.py

n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

result = 0
arr.sort(reverse=True)
for i in arr:
    if k==0: break
    result += k // i
    k %= i
print(result)