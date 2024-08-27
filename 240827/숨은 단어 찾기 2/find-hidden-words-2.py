n,m = tuple(map(int,input().split()))

arr = []

#문제 배열 선언
for k in range(n):
    arr.append([])
    char = input()
    for l in range(m):
        arr[k].append(char[l])

# 배열의 범위 내에 있는 지 확인
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

# 이동 방향을 배열로 지정
dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]

answer = 0

# 
for i in range(n):
    for j in range(m):

        # 배열을 값이 'L' 일 때 탐색
        if arr[i][j] == 'L':

            # 360도로 회전하며 탐색한다
            for dx,dy in zip(dxs,dys):
                curx = i
                cury = j
                cnt = 0 #'E'의 갯수

                # 배열의 범위 내에 있고, 배열의 값이 'E'라면 count
                while in_range(curx+dx,cury+dy) and arr[curx+dx][cury+dy] == 'E':
                    cnt += 1
                    # 위치 이동
                    curx = curx+dx
                    cury = cury+dy
                    
                    #'E'의 갯수가 2개라면 갯수를 세고 탐색을 종료한다
                    if cnt == 2:
                        answer += 1
                        break

print(answer)