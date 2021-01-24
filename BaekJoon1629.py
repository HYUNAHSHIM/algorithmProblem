# BaekJoon 1629 곱셈

def multiple(a, b):
    # b가 1이면 곱해줄 필요가 없으므로 a % C를 리턴
    if b == 1:
        return a % C
    else:
        # a^b를 구할때 (a^(b/2))^2에서 a^(b/2)를 먼저 계산해줘서 활용
        value = multiple(a, b // 2)
        # (a^(b/2))2을 할때, b가 짝수인 경우, b/2가 나머지 없이 나눠지므로 ( a^(b/2) * a^(b/2) ) / c를 해줌
        if b % 2 == 0:
            return value * value % C
        # (a^(b/2))2을 할때, b가 홀수인 경우, b/2가 나머지 1이게 나눠지므로 ( a^(b/2) * a^(b/2) * a ) / c를 해줌
        else:
            return value * value * a % C


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(multiple(A, B))
