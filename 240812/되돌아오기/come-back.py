#방향에 따른 인덱스 설정
direction = {
    'E':0,
    'S':1,
    'W':2,
    'N':3
}

# 이동방향
mov_x = [1,0,-1,0]
mov_y = [0,-1,0,1]

#x,y좌표 초기값
x,y = 0, 0

n = int(input())
t = 0

# 주어진 지문을 리스트에 담는다. 두번째 요소는 정수로 변환해서 담는다.
ques = []
for _ in range(n):
    ques.append(list(input().split()))
    ques[-1][1] = int(ques[-1][1])


ans = -1

# 지문을 순회하며 이동한다. 
for arr in ques:
    dir_num = direction[arr[0]]
    for n in range(arr[1]):
        t += 1
        x += mov_x[dir_num]
        y += mov_y[dir_num]
        # 이동 후 x,y 가 0이 되는 순간 break
        if x == 0 and y == 0:
            ans = t
            break

# 정답 출력
print(ans)