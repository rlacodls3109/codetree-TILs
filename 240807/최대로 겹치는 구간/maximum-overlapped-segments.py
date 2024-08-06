n = int(input())

#가장 많이 겹치는 구간의 선분 개수를 찾기 위한 함수
def find_max(arr):
    max = 0
    for elem in arr:
        if elem > max:
            max = elem
    
    return max

# -100 <= x1 < x2 <= 100 이므로 201개의 요소를 가진 배열을 선언한다.
# arr[100] 이 0으로, 적은 인덱스는 음수, 큰 인덱스는 양수로 생각한다.
arr = [0] * 201

for _ in range(n):
    x1, x2 = tuple(map(int,input().split()))
    
    # 겹치는 구간을 찾으려면 각 구간의 시작위치만 표시하면 된다. x1 ~ x2-1
    for i in range(x1,x2):
        #0이 인덱스 100이므로 지점에 +100을 해준다.
        arr[i+100] += 1


result = find_max(arr)
print(result)