OFFSET = 100000
MAX_R = 200000

n = int(input())

#-1이면 회색, 0이면 흰색, 1이면 검은 색
Color = [-1] * (MAX_R + 1)
#현 위치는 ~100000~100000 중 0
current_pos = OFFSET

for _ in range(n):
    x, M = tuple(input().split())
    x = int(x)

    # L이면 현위치에서 왼쪽으로 이동하며 타일을 하얀색(0)으로 변경한다.
    if M == 'L':
        for i in range(current_pos,current_pos-x,-1):
            Color[i] = 0 
        current_pos -= (x-1) # 현 위치 변경
    
    # R이면 현위치에서 오른쪽으로 이동하며 타일을 검은색(1)으로 변경한다.
    elif M =='R':
        for i in range(current_pos,current_pos+x):
            Color[i] = 1
        current_pos += (x-1) # 현 위치 변경

#타일 색상 세기 위한 배열
count_col = [0,0]

for elem in Color:
    if elem == -1: # 타일이 회색일 때에는 세지 않는다.
        continue
    else:
        count_col[elem] += 1 # 타일 색상의 갯수를 센다

for elem in count_col:
    print(elem, end = " ")