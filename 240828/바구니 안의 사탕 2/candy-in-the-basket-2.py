MAX_BASKET = 100

n, k = tuple(map(int,input().split()))

# 바구니의 위치 배열
# 위치는 1부터 시작하므로 0번째 배열위치는 비워둔다
arr = [0] * (MAX_BASKET+1)
sum_candy = 0
# 입력되는 사탕의 정보를 배열에 저장한다.
for _ in range(n):
    candy, pos_basket = tuple(map(int,input().split()))
    sum_candy += candy
    arr[pos_basket] += candy

result_max = -1

# k(배열의 구간) 값이 50 이상이면 전체 사탕의 갯수가 답이 된다.
if k >= 50:
    result_max = sum_candy

else: 
    # i는 탐색할 구간의 시작 위치
    # c-k ~ c+k를 탐색할 것이므로 탐색 시작 위치는 0 + k 여야 한다.
    for i in range(k+1,MAX_BASKET-k-1):
        count_candy = 0
        # 구간 탐색
        for j in range(i-k,i+k+1):
            count_candy += arr[j]
        
        # 최댓값 갱신
        result_max = max(result_max,count_candy)

print(result_max)