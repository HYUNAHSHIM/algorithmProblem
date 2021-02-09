# BaekJoon 6603.py 로또

def solve():
    if len(out) == 6:  # 길이가 6인 리스트가 완성되었다면
        print(' '.join(map(str, out)))  # 출력
        return
    for i in range(length):  # 1-n까지 수를 돌아가며
        if visited[i]: # 이미 사용한 값이면 pass
            continue
        if len(out) != 0 and out[-1] > li[i]: # 선택된 숫자들 중 가장 마지막 숫자가 현재 선택 예정인 숫자보다 크면 사전순이 아니니까 pass
            continue
        out.append(li[i])  # 사용한 것 리스트에 기록
        visited[i] = True
        solve()  # 리스트의 다음 수 정하러 들어감
        out.pop()  # k번째 수를 i로 정한 경우를 모두 확인했으므로 k번째 수를 pop하기(다음 수를 k번째에 집어넣기 위해)
        visited[i] = False


inputLi = list(map(int, input().split()))
if inputLi[0] == 0:
    exit()
li = inputLi[1:]
length = len(li)
out = [] # 선택한 숫자들 저장 위해
visited = [False] * length # 사용한 것 기록하기 위해
while inputLi[0] != 0:
    solve()
    inputLi = list(map(int, input().split())) # 다음 test case 받기
    li = inputLi[1:]
    length = len(li)
    visited = [False] * length
    out = []
    print()
