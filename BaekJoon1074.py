# BaekJoon1074.py

N, r, c = map(int, input().split())
result = 0

while N > 1:
    size = (2 ** N) // 2
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        result += size ** 2
        c -= size
    elif r >= size and c < size:
        result += size ** 2 * 2
        r -= size
    elif r >= size and c >= size:  # 4사분면
        result += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    print(result)
if r == 0 and c == 1:
    print(result + 1)
if r == 1 and c == 0:
    print(result + 2)
if r == 1 and c == 1:
    print(result + 3)