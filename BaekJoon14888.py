# BaekJoon14888.py

N = int(input())
arr = list(map(int, input().split()))  # 숫자들
ops = list(map(int, input().split()))  # + - * % 의 개수
max_result = float('-inf')
min_result = float('inf')


def dfs(lis):
    global ops, arr, max_result, min_result

    # 모든 연산자가 사용된 경우
    if len(lis) == len(arr) - 1:
        result = arr[0]
        for idx, op in enumerate(lis):
            if op == 0:
                result += arr[idx + 1]
            elif op == 1:
                result -= arr[idx + 1]
            elif op == 2:
                result *= arr[idx + 1]
            elif op == 3:
                if result < 0:
                    result = -1 * ((result * -1) // arr[idx + 1])
                else:
                    result //= arr[idx + 1]
        max_result = max(max_result, result)
        min_result = min(min_result, result)

    for i in range(4):
        if ops[i] == 0:
            continue
        ops[i] -= 1
        dfs(lis + [i])
        ops[i] += 1


dfs([])
print(max_result)
print(min_result)
