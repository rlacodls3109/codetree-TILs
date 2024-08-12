n = int(input())

coin = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_cnt = 0
for i in range(n):
    coin_cnt = 0
    for j in range(n-2):
        coin_cnt = coin[i][j] + coin[i][j+1] + coin[i][j+2]
    
    max_cnt = max(max_cnt,coin_cnt)

print(max_cnt)