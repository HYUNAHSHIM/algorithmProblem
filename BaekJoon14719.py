# BaekJoon14719.py

H, W = map(int, input().split())
arr = list(map(int, input().split()))


def solve():
    global W, arr
    result = 0
    for i in range(W):
        max_left = max(arr[:i+1])
        max_right = max(arr[i:])
        lowest = min(max_left, max_right)
        result += abs(arr[i] - lowest)
    return result


print(solve())
