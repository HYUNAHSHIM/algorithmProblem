# BaekJoon 15649.py N과 M(2)
# 백트래킹 문제: 주어진 문제의 답을 구하기 위해 현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘

n, m = map(int, input().split())
visited = [False] * n  # 사용 여부 확인용
out = []  # 출력 내용


def solve(depth, N, M):
    if depth == M:  # 길이가 m인 리스트가 완성되었다면
        print(' '.join(map(str, out)))  # 출력
        return
    for i in range(n): # 1-n까지 수를 돌아가며
        if not visited[i]:  # i 값 사용을 아직 하지 않았다면
            if len(out) != 0 and out[-1] > i: # 오름차순 배열을 위해 넣을 값이 현재 있는 값의 가장 큰 값보다 작으면 pass
                continue
            visited[i] = True  # i 사용 여부 true
            out.append(i+1)  # 사용한 것 리스트에 기록
            solve(depth+1, N, M)  # 리스트의 다음 수 정하러 들어감
            visited[i] = False  # k번째 수를 i로 정한 경우를 모두 확인했으므로 i를 이제 사용x
            out.pop()  # k번째 수를 i로 정한 경우를 모두 확인했으므로 k번째 수를 pop하기(다음 수를 k번째에 집어넣기 위해)


solve(0, n, m)
