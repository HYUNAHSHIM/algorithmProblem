# Programmers_행렬테두리회전.py

def rotate(arr, query):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = query[0] - 1, query[1] - 1
    pre_value = arr[x][y]
    len_x = query[3] - query[1]
    len_y = query[2] - query[0]
    left = len_x
    direction = 0

    length = 2 * (len_x + 1) + 2 * (len_y + 1) - 4
    min_value = pre_value
    for _ in range(length):
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 최소값 갱신
        min_value = min(min_value, arr[nx][ny])
        # 변경할 자리에 있는 값 저장하고 변경
        tmp = pre_value
        pre_value = arr[nx][ny]
        arr[nx][ny] = tmp
        x = nx
        y = ny
        # 회전 정보 변경
        left -= 1
        if left == 0:
            direction = (direction + 1) % 4
            if direction == 0 or direction == 2:
                left = len_x
            else:
                left = len_y
    return arr, min_value


def solution(rows, columns, queries):
    answer = []

    # 배열 초기화
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1

    # query 수행
    for query in queries:
        arr, smallest = rotate(arr, query)
        answer.append(smallest)

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
