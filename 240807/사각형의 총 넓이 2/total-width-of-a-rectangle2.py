OFFSET = 1000

N = int(input())

# 코드를 맞게 입력한 것 같은데 arr[i][j]를 변경하니 같은 열의 값들이 모두 변경되는 오류... why?
# (틀린부분) list는 mutable 하므로 복사되면 같은 주소를 공유하게 되어 한 곳의 값이 바뀌면 다른 쪽도 바뀐다.
#y_arr = [0] * (2*OFFSET + 1)
#rec_arr = [y_arr] * (2*OFFSET + 1)
rec_arr = [
    [0]*(2*OFFSET +1)
    for _ in range(2*OFFSET + 1) #2차원 배열을 선언할 때 배열의 곱하기로 하면 deep copy됨. 반드시 포문으로!
]

for _ in range(N):
    x1, y1, x2, y2 = tuple(map(int,input().split()))

    #(x1,y1),(x2,y2)로 이루어진 사각형은 2차원 격자 상에서 (x1,y1)~(x2-1,y2-1) 까지로 이루어진다.
    for i in range(x1+OFFSET,x2+OFFSET):
        for j in range(y1+OFFSET,y2+OFFSET):
            # 겹치는 부분은 한번만 체크해야 한다.
            if rec_arr[i][j] == 0:
                rec_arr[i][j] += 1
                
#체크된 구간 갯수 세서 출력
cnt = 0
for arr in rec_arr:
    for elem in arr:
        if elem == 1:
            cnt += 1
print(cnt)