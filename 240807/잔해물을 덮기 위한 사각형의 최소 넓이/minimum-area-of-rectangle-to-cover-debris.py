OFFSET = 1000

rec = [
    [0] * (2*OFFSET + 1)
    for _ in range(2*OFFSET + 1)
]

#k = 1, 2에 대해서 동작 수행
for k in range(1,3):
    x1, y1, x2, y2 = tuple(map(int,input().split()))

    for i in range(x1+OFFSET,x2+OFFSET):
        for j in range(y1+OFFSET,y2+OFFSET):
            # 1일 때 첫번째 사각형 2일 때 그 위에 얹어진 두번째 사각형
            rec[i][j] = k



max_x = -1
min_x = 2*OFFSET+1
max_y = -1
min_y = 2*OFFSET+1

for x in range(0,2*OFFSET+1):
    for y in range(0,2*OFFSET+1):
        if rec[x][y] == 1:
            if x >= max_x:
                max_x = x+1
            if x <= min_x:
                min_x = x
            if y >= max_y:
                max_y = y+1
            if y <= min_y:
                min_y = y

area = (max_x-min_x) * (max_y-min_y)
print(area)