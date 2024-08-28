n = int(input())

arr = list(map(int,input().split()))

result = 0

# k = 탐색할 구간의 길이
for k in range(1,n+1):
    # i = 구간의 시작점
    for i in range(0,n-k+1):
        sum_num = 0

        # 구간을 탐색하며 구간의 합을 구한다
        for j in range(i,i+k):
            sum_num += arr[j]
        
        # 평균을 구한다
        avg_num = sum_num/k

        # 문제의 조건을 만족하는 지 확인하는 bool 변수
        check_con = False

        # 구간을 탐색하며 조건에 만족하는 지 확인한다.
        for l in range(i,i+k):
            if avg_num == arr[l]:
                check_con = True
        
        # 조건에 만족하면 카운트
        if check_con:
            result += 1

print(result)