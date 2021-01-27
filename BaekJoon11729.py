# BaekJoon 11729 하노이의 탑 이동 순서

def hanoi(n, a, b, c):
    # 원판이 한개인 경우는 한번만 옮기면 되므로 따로 처리
    if n == 1:
        print(a, c)
    # a기둥에 n개의 원판이 있을 때 c 기둥으로 옮기려면
    else:
        # n-1개를 b기둥으로 옮기고
        hanoi(n-1, a, c, b)
        # 나머지 가장 큰 한개를 c로 옮기고
        print(a, c)
        # b기둥에 있는 n-1개를 c로 옮기면 된다
        hanoi(n-1, b, a, c)

if __name__ == "__main__":
    n = int(input())
    # 총 횟수를 구해보자
    sum = 1
    for i in range(n - 1):
        # n-1개를 옮기는 것 두번 + 가장 큰 한개를 옮기는 것 한번
        sum = sum * 2 + 1
    print(sum)
    # 과정을 구해보자
    hanoi(n, 1, 2, 3)