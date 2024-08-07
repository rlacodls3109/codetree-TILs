OFFSET = 10
MAX_R = 2*OFFSET

rec = [
    [-1] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

n = int(input())

# 빨간색 -> 파란색 순서이므로
# i % 2 == 0일 때 빨간색, 1일 때 파란색
for i in range(n):
    x1, y1, x2, y2 = tuple(map(int,input().split()))

    for x in range(x1+OFFSET,x2+OFFSET):
        for y in range(y1+OFFSET, y2+OFFSET):
            rec[x][y] = i #차례대로 해당 영역 값을 i로 갱신한다.


# 파란색 영역 구하기
area = 0

for j in range(MAX_R+1):
    for k in range(MAX_R+1):
        # 한 번 이상 채워진 영역이면서, 파란색인 영역을 센다
        if rec[j][k] != -1 and rec[j][k] % 2 == 1:
            area += 1

print(area)