n = int(input())

# 주어진 동전 정보
coin = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_cnt = 0
for i in range(n):
    coin_cnt = 0
    # 격자를 벗어나는 경우는 제외해야 함에 유의 가로 3의 길이이므로 최대 시작 인덱스가 n-3여야 함
    for j in range(n-2):
        coin_cnt = coin[i][j] + coin[i][j+1] + coin[i][j+2]
        max_cnt = max(max_cnt,coin_cnt)

print(max_cnt)