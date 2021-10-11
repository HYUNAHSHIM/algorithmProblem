# BaekJoon1541.py

arr = input().split("-")
results = []
for i in arr:
    cnt = 0
    b = i.split("+")
    for j in b:
        cnt += int(j)
    results.append(cnt)
first = results[0]
for i in range(1, len(results)):
    first -= results[i]
print(first)