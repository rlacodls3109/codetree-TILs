MAX_LINE = 100
n,k = tuple(map(int,input().split()))

arr = [0] * MAX_LINE

#문제에서 주어진 조건을 배열에 저장한다.
for _ in range(n):
    given = list(input().split())
    arr[int(given[0])-1] = given[1]

result = -1

#배열을 탐색. 탐색 구간에 따라 for문의 범위를 설정한다.
for i in range(len(arr)-k):
    score = 0
    # 시작점에서 사진의 길이만큼 탐색하며 점수를 계산한다.
    # 문제에서 사진의 크기란 양쪽 끝에 있는 x값끼리의 차로 정의했으므로 for문의 범위에 유의
    for j in range(i,i+k+1):
        if arr[j] == 'G': # 'G'면 1점
            score += 1
        elif arr[j] == 'H': #'H'면 2점
            score += 2
        else: 
            continue
    # 최댓값 갱신
    result = max(result,score)
    
print(result)