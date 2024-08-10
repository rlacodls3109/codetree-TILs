n = int(input())

arr = []

#dxs는 행의 이동, dys는 열의 이동
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

#인덱스가 행렬의 범위 내에 있는 지 확인하는 함수
def in_range(row,col):
    return 0 <= row and row < n and 0 <= col and col < n

for _ in range(n):
        arr.append(list(map(int,input().split())))

ans = 0

#주어진 행렬 순회
for row in range(n): #행
    for col in range(n): #열
        cnt = 0 #각 요소마다 cnt 초기화
        for dx,dy in zip(dxs,dys):
            n_row, n_col = row+dx, col+dy #각 요소의 상하좌우 위치
            if in_range(n_row,n_col) and arr[n_row][n_col] == 1:
                cnt += 1
        
        # 만약 3개 이상이라면
        if cnt >= 3:
            ans += 1

print(ans)