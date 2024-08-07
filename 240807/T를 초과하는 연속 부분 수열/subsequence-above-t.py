n, t = tuple(map(int,input().split()))

arr = list(map(int,input().split()))

cnt = 0
max_cnt = 0


for i in range(n):
    # 현재 원소가 t보다 크다면 카운트
    if arr[i] > t :
        cnt += 1
    # 작다면 cnt 초기화
    else: 
        cnt = 0
    
    max_cnt = max(max_cnt,cnt)


print(max_cnt)