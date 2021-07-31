# BaekJoon2630.py

def checkSame(n, x, y):
    global arr
    value = arr[x][y]
    for i in range(n):
        for j in range(n):
            if arr[x + i][y + j] != value:
                return False
    return True


def solv(n, x, y):
    global arr, white, blue
    if checkSame(n, x, y):
        if arr[x][y] == 0:
            white += 1
        else:
            blue += 1
    else:
        new_n = int(n / 2)
        solv(new_n, x, y)
        solv(new_n, x + new_n, y)
        solv(new_n, x, y + new_n)
        solv(new_n, x + new_n, y + new_n)


N = int(input())
arr = [0 for _ in range(N)]
white = 0
blue = 0

for i in range(N):
    arr[i] = list(map(int, input().split()))

solv(N, 0, 0)
print(white)
print(blue)
