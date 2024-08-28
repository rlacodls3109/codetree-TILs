n, m = tuple(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

result = 0

# i = 구간의 시작점
for i in range(n-m+1):
    # 아름다운 수열이 존재하는 지 확인하기 위한 bool 함수
    check_in_B = True

    # 탐색할 때 사용할 새로운 리스트를 만든다.
    new_B = [
            B[i]
            for i in range(len(B))
        ]
    
    # 수열 A에 대해 구간탐색
    for j in range(i,i+m):
        
        # B에 있는 값이 아니라면 즉시 탐색을 종료한다.
        if A[j] not in new_B:
            check_in_B = False
            break
        # B에 있는 값이라면 new_B에서 요소를 제거한다
        new_B.remove(A[j])

    if check_in_B :
        result += 1

print(result)