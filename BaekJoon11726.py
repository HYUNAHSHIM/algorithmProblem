# BaekJoon11726.py

arr = [0, 1, 2]
for i in range(3, 1001):
  arr.append(arr[i - 2] + arr[i - 1])
n = int(input())
print(arr[n] % 10007)