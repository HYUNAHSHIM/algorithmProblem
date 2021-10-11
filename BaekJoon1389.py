# BaekJoon 1389 케빈 베이컨의 6단계 법칙
from collections import deque

if __name__ == "__main__":

    answer = [0, 100000]
    N, M = map(int, input().split())
    arr = {}

    # 초기화, 인접 리스트
    for i in range(M):
        a, b = map(int, input().split())
        if a in arr:
            arr[a].append(b)
        else:
            arr[a] = [b]
        if b in arr:
            arr[b].append(a)
        else:
            arr[b] = [a]

    for i in range(N):
        tmp_result = 0
        for j in range(N):
            if i == j:
                continue
            visited = {}
            queue = deque()
            for key in arr.keys():
                visited[key] = False

            # 초기값 push
            queue.append([list(arr.keys())[i], 0])
            visited[list(arr.keys())[i]] = True

            # 큐가 빌때까지 반복
            while len(queue) != 0:
                value = queue.popleft()

                # 최단 경로 찾으면 단계 추가 후 break
                if value[0] == list(arr.keys())[j]:
                    tmp_result = tmp_result + value[1]
                    break

                # 이어서 연결된 다음 친구로
                for k in arr[value[0]]:
                    if visited[k] is False:
                        queue.append([k, value[1] + 1])
                        visited[k] = True

        # i번이 케빈 베이컨의 수가 가장 작은지 확인
        # 작은게 여러개라면 숫자가 작은걸로
        if tmp_result < answer[1]:
            answer[0] = list(arr.keys())[i]
            answer[1] = tmp_result
        elif tmp_result == answer[1]:
            if list(arr.keys())[i] < answer[0]:
                answer[0] = list(arr.keys())[i]

    print(answer[0])
