# BaekJoon 2352.py

N = int(input())
arr = list(map(int, input().split()))
lst = []


# 이분 탐색
def find(s, e, v):
    global lst
    while s < e:
        m = (s + e) // 2
        if lst[m] < v:
            s = m + 1
        else:
            e = m
    return e


for i in range(N):
    # 첫번째 숫자인 경우
    if i == 0:
        lst.append(arr[i])
    else:
        # 증가하는 수열이면
        if arr[i] > lst[-1]:
            lst.append(arr[i])
        # 감소하는 수열이면 이분탐색으로 자리 찾기
        else:
            # 0부터 len(lst)사이의 lst배열에서 arr[i]의 위치 찾아서 lst에 넣어주기기
            lst[find(0, len(lst), arr[i])] = arr[i]

print(len(lst))
