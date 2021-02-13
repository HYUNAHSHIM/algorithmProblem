# BaekJoon1759.py 암호 만들기

l, c = map(int, input().split())
arr = sorted(input().split())
visited = [False] * c # 사용 여부 저장
vowel = ['a', 'e', 'i', 'o', 'u'] # 모음
consonant_n = 0 # 자음 개수
vowel_n = 0 # 모음 개수
out = [] # 출력 배열 저장


def solve(con, vow):
    if len(out) is l:
        # 최소 한개의 모음, 최소 두개의 자음으로 구성하기 위한 조건
        if con > 1 and vow > 0:
            print(''.join(map(str, out)))
        return
    else:
        for i in range(c):
            # 방문했다면 pass
            if visited[i]:
                continue
            # 사전순으로 구성하기 위한 조건
            if len(out) != 0 and out[-1] > arr[i]:
                continue
            # 방문했다고 표시
            visited[i] = True
            out.append(arr[i])
            # 모음, 자음 여부 기록
            if arr[i] in vowel:
                vow += 1
                # 다음 문자 정하기 위해
                solve(con, vow)
                vow -= 1
            else:
                con += 1
                solve(con, vow)
                con -= 1
            visited[i] = False
            out.pop()


solve(consonant_n, vowel_n)
