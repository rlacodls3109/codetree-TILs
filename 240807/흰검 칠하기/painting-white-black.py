OFFSET = 100000
MAX_R = 200000

# n번의 명령
n = int(input())
White = [0] * (MAX_R + 1)
Black = [0] * (MAX_R + 1)
Color = [-1] * (MAX_R + 1) # 0이면 흰, 1이면 검, 2면 회색

current_pos = OFFSET

# White[i] >= 2 and Black[i] >= 2 이면 Color[i] = 2
def check_gray(White,Black,i):
    if White[i] >= 2 and Black[i] >= 2:
        Color[i] = 2

for _ in range(n):
    x, M = tuple(input().split())
    x = int(x)
    
    '''
    #배열 체크하는 코드
    print("W", White[OFFSET-6:OFFSET+6:]) 
    print("B", Black[OFFSET-6:OFFSET+6:]) 
    print("C", Color[OFFSET-6:OFFSET+6:]) 
    '''

    # M = L이면 흰색으로 현위치타일부터 왼쪽으로 x칸 만큼 칠함
    if M == 'L':
        for i in range (current_pos,current_pos-x,-1):
            if Color[i] != 2: #i번째 타일의 색이 회색이 아닐 때에만 흰색으로 변경하는 작업을 한다.
                White[i] += 1
                # Color[i] = 0으로 변경
                Color[i] = 0
                #회색 타일로 변경해야 하는 지 체크
                check_gray(White,Black,i)
        #현 위치 변경
        current_pos -= (x-1)

    # M = R이면 검은색으로 현위치타일부터 오른쪽으로 x칸 만큼 칠함
    elif M == 'R':
        for i in range (current_pos,current_pos+x):
            if Color[i] != 2: #i번째 타일이 회색이 아닐 때에만 검정색을 변경한다.
                Black[i] += 1
                # Color[i] = 1으로 변경
                Color[i] = 1
                #회색 타일로 변경해야 하는 지 체크
                check_gray(White,Black,i)
        
        #현 위치 변경
        current_pos += (x-1)

# W,B,G 색 타일 count하는 배열
count_arr = [0,0,0]

# Color 배열을 돌며 타일 색상의 개수를 센다
for col in Color:
    if col == 0:
        count_arr[0] += 1
    elif col == 1:
        count_arr[1] += 1
    elif col == 2:
        count_arr[2] += 1
    else:
        continue

for elem in count_arr:
    print(elem, end=" ")