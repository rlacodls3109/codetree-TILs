N, k = tuple(map(int,input().split()))

#각 칸의 블럭 중 최댓값을 찾는 함수
def search_max(arr):
    max = 0

    for elem in arr:
        if elem > max : 
            max = elem
    
    return max

# 0으로 이루어진 N+1 길이의 배열을 선언한다. 인덱스가 0부터 시작하기 때문
arr = [0] * (N+1)

# k번 블럭을 쌓는 명령을 수행함
for i in range(k):
    a, b = tuple(map(int,input().split()))
    for j in range(a,b+1): 
        arr[j] += 1 #a번 칸부터 b번 칸까지 블럭을 하나 씩 샇는다.

#결과 값 가져오기
result = search_high(arr)
print(result)