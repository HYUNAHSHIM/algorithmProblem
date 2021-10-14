# BaekJoon21608.py


# 초기값 설정
N = int(input())
positions = [[0 for _ in range(N)] for _ in range(N)]
likes = {}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N * N):
    arr = list(map(int, input().split()))
    likes[arr[0]] = arr[1:]


# 좋아하는 학생이 인접한 칸에 가장 많은 칸 선택해서 return
def like_max(arr):
    global positions, N, dx, dy

    like_arr = {}
    for x in range(N):
        for y in range(N):
            # 비어있지 않은 자리면 pass
            if positions[x][y] != 0:
                continue
            like_student_num = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 교실 밖으로 벗어난다면
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                # 좋아하는 학생이 앉아있다면 +1
                if positions[nx][ny] in arr:
                    like_student_num += 1
            # 좋아하는 학생수 추가
            if like_student_num in like_arr:
                like_arr[like_student_num].append([x, y])
            else:
                like_arr[like_student_num] = [[x, y]]

    # 좋아하는 학생 수가 최대인 자리 return
    return like_arr[max(like_arr.keys())]


# 인접한 칸 중 비어있는 칸 가장 많은 칸 선택해서 return
def empty_max(arr):
    global positions, N, dx, dy

    empty_arr = {}
    for x, y in arr:
        empty_num = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 교실 밖으로 벗어난다면
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if positions[nx][ny] == 0:
                empty_num += 1
        if empty_num in empty_arr:
            empty_arr[empty_num].append([x, y])
        else:
            empty_arr[empty_num] = [[x, y]]

    # 인접한 칸 중 비어있는 칸 가장 많은 자리 return
    return empty_arr[max(empty_arr.keys())]


# 행이 가장 작은 칸 return. 만약 같다면 열이 가장 작은 칸 return
def smallest_position(arr):
    return sorted(arr, key=lambda x: (x[0], x[1]))[0]


# 만족도 계산해서 return
def cal_satisfy():
    global positions, likes, N, dx, dy

    result = 0
    for x in range(N):
        for y in range(N):
            student = positions[x][y]
            like = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if positions[nx][ny] in likes[student]:
                    like += 1

            # 인접한 좋아하는 학생수에 따라 계산
            if like == 1:
                result += 1
            elif like == 2:
                result += 10
            elif like == 3:
                result += 100
            elif like == 4:
                result += 1000

    return result


def solve():
    global likes, positions
    students = likes.keys()

    for student in students:
        like_max_list = like_max(likes[student])
        if len(like_max_list) == 1:
            selected = like_max_list[0]
        else:
            empty_max_list = empty_max(like_max_list)
            if len(empty_max_list) == 1:
                selected = empty_max_list[0]
            else:
                selected = smallest_position(empty_max_list)

        positions[selected[0]][selected[1]] = student

    print(cal_satisfy())


solve()
