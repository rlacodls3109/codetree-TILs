import sys

arr = list(map(int,input().split()))

#세 숫자로 이루어진 두 팀의 차를 계산하는 함수
def get_diff(a,b,c):
    sum1 = arr[a] + arr[b] + arr[c]
    sum2 = sum(arr) - sum1
    return abs(sum1-sum2)

result = sys.maxsize


for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            result = min(result,get_diff(i,j,k))

print(result)