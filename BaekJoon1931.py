# BaekJoon1931.py


def solution(arr):
    answer = 0
    endTime = 0
    for i in range(len(arr)):
        # 회의가 시작하는 시간이 이전 회의가 끝나는 시간보다 늦거나 같다면 가능하니까 추가
        if endTime <= arr[i][0]:
            endTime = arr[i][1]
            answer += 1
    return answer


N = int(input())
arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

# 빨리 끝나는 순 -> 빨리 시작하는 순으로 정렬
arr.sort(key=lambda x: (x[1], x[0]))
print(solution(arr))
