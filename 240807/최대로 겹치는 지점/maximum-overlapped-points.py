def find_max(arr):
    max = 0
    for elem in arr:
        if max < elem :
            max = elem
    return max

n = int(input())

#인덱스가 0부터 시작하므로 101개의 요소를 가지는 배열 선언
arr = [0] * 101

for _ in range(n):
    x1, x2 = tuple(map(int,input().split()))
    # 끝 점에서 닿는 경우에도 겹치는 것으로 보므로 x1 ~ x2까지의 지점을 모두 표시해야 함
    for i in range(x1,x2+1):
        arr[i] += 1
    
#결과
result = find_max(arr)
print(result)