OFFSET = 1000

#좌표평면을 나타내는 2차원 배열 선언
rec = [
    [0] * (2*OFFSET + 1)
    for _ in range(2*OFFSET + 1)
]

#k = 1, 2에 대해서 동작 수행
for k in range(1,3):
    x1, y1, x2, y2 = tuple(map(int,input().split()))

    #격자 단위로 진행하는 문제이므로 x2,y2에 등호가 들어가지 않음에 유의
    for i in range(x1+OFFSET,x2+OFFSET):
        for j in range(y1+OFFSET,y2+OFFSET):
            # 1일 때 첫번째 사각형, 2일 때 그 위에 얹어진 두번째 사각형
            rec[i][j] = k


#1로 표시된 부분의 최대, 최소 x,y 값 구하기
max_x = -1
min_x = 2*OFFSET+1
max_y = -1
min_y = 2*OFFSET+1
cnt = 0 # 1이 존재하는 지 검사하기 위한 변수

#전체 배열을 순회한다.
for x in range(0,2*OFFSET+1):
    for y in range(0,2*OFFSET+1):
        #1이 존재한다면
        if rec[x][y] == 1:
            '''
            if x >= max_x:
                max_x = x
            if x <= min_x:
                min_x = x
            if y >= max_y:
                max_y = y
            if y <= min_y:
                min_y = y
            cnt += 1
            '''
            # x,y 값을 갱신한다
            # min,max 함수로 간단하게 표현
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            cnt += 1

# 잔해물 덮기 위한 직사각형의 넓이 계산 
# cnt가 0이면 1이 존재하지 않는 것임
if cnt == 0:
    area = 0 # 넓이는 0이 된다

else : 
    # 격자 단위로 진행하였으므로 max값에 +1을 해줘야 직사각형의 넓이를 제대로 구할 수 있다.
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    
print(area)