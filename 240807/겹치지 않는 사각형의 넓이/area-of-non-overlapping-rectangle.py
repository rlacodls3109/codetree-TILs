OFFSET = 1000

# 사각형의 넓이를 구하기 위한 배열 선언
rec = [
    [0] * (2*OFFSET + 1)
    for _ in range(2*OFFSET + 1)
]

#사각형의 넓이를 칠하는 함수
#이때 ~x2-1, ~y2-1 까지임을 유의
def draw_rec(x1,y1,x2,y2):
    for i in range(x1+OFFSET,x2+OFFSET):
        for j in range(y1+OFFSET,y2+OFFSET):
            if rec[i][j] == 0:
                rec[i][j] = 1

#겹치는 부분 제외하는 함수
#이때 ~x2-1, ~y2-1 까지임을 유의
def remove_rec(x1,y1,x2,y2):
    for i in range(x1+OFFSET,x2+OFFSET):
        for j in range(y1+OFFSET,y2+OFFSET):
            if rec[i][j] == 1: #1일 때 다시 0으로 바꾸어준다
                rec[i][j] = 0

rec_A = tuple(map(int,input().split()))
draw_rec(rec_A[0],rec_A[1],rec_A[2],rec_A[3]) # 직사각형 A 칠하기

rec_B = tuple(map(int,input().split()))
draw_rec(rec_B[0],rec_B[1],rec_B[2],rec_B[3]) #직사각형 B 칠하기

rec_M = tuple(map(int,input().split()))
remove_rec(rec_M[0],rec_M[1],rec_M[2],rec_M[3]) #직사각형 M 제외하기

#넓이 구하기
area = 0
for arr in rec:
    for elem in arr:
        if elem == 1:
            area += 1

print(area)