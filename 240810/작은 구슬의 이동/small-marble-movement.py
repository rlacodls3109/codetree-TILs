# 딕셔너리로 방향 - 인덱스 저장
 # 왼 - 오 / 위 - 아래에 대해 방향 전환이 필요하므로 적절한 인덱스 설정이 필요함
mapper = {
    'U' : 0,
    'R' : 1, 
    'L' : 2,
    'D' : 3
}

dx,dy = [-1, 0, 0, 1],[0, 1, -1, 0]

# 범위 내에 있는 지 확인하는 함수
def in_range(r,c,n):
    return 0 <= r and r < n and 0 <= c and c < n

n, t = tuple(map(int,input().split()))
r,c,d = tuple(input().split())

#1행 1열은 (0,0)
r,c = int(r)-1, int(c)-1
now_d = mapper[d]

for _ in range(t):
    # 한 칸 이동 시 위치
    n_r, n_c = r + dx[now_d], c + dy[now_d]

    # 이동했는데 배열의 범위 밖으로 벗어나면 방향 반대로 변경
    if not in_range(n_r,n_c,n):
        now_d = 3 - now_d
    # 범위 내라면 이동을 확정
    else:
        r, c = n_r, n_c

print(r+1, c+1)