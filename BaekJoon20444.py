# BaekJoon20444.py

n, k = map(int, input().split())


def solve():
    global n, k
    value = (n + 2) ** 2 - 4 * k

    # 근이 무리수가 아니어야함
    if value < 0:
        print("NO")
        return

    # 근이 정수여야 함
    if int(value ** 0.5) ** 2 != value:
        print("NO")
        return

    first = ((n + 2) - value ** 0.5) / 2
    second = ((n + 2) + value ** 0.5) / 2

    # 2로 나눴을 때 정수여야 함
    if int(first) != first or int(second) != second:
        print("NO")
        return

    # 근이 자연수여야 함
    if first > 0 and second > 0:
        print("YES")
        return

    print("NO")

solve()
