# BaekJoon 1992.py


def solution(arr, pos, x, y, result):
    if pos == 1:
        return result + str(arr[y][x])
    # 모두 같은지 체크
    is_same = True
    value = arr[y][x]
    for i in range(pos):
        for j in range(pos):
            if arr[y+i][x+j] != value:
                is_same = False
    # 같으면
    if is_same:
        return result + str(arr[y][x])
    # 다르면
    elif not is_same:
        result = result + "("
        result = solution(arr, int(pos / 2), x, y, result)
        result = solution(arr, int(pos / 2), int(x + (pos / 2)), y, result)
        result = solution(arr, int(pos / 2), x, int(y + (pos / 2)), result)
        result = solution(arr, int(pos / 2), int(x + (pos / 2)), int(y + (pos / 2)), result)
    result = result + ")"
    return result


N = int(input())
image = [list(map(int, input())) for _ in range(N)]
r = solution(image, N, 0, 0, "")
print(r)
