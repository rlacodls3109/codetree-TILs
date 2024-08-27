# 코드 줄이기!!!!!!!!

n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

result = 0
# step1. 첫번째 격자를 놓는다. (i,j)
for i in range(n):
    for j in range(n-2):
        # 두번째 격자를 놓는다. (k,l)
        for k in range(n):
            for l in range(n-2):
                # step2. 두 격자가 겹치면 카운트 하지 않는다.
                if i == k and abs(j-l) <=2:
                    continue
                
                #step3. 두 격자가 겹치지 않는 경우에 대해 동전 수를 세어 갱신한다.
                cnt1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                cnt2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]

                result = max(result,cnt1+cnt2)

print(result)

'''
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

result = 0

# 배열 탐색
for i in range(n):
    for j in range(n):
        cnt1 = 0

        # step1. j+2가 범위 내에 있는 값이라면 첫번째 격자를 배치
        if in_range(i,j+2):
            cury1 = j
            while(1):
                # 동전이 있으면 카운트
                if arr[i][cury1] == 1:
                    cnt1 += 1
                # 격자의 길이가 3이므로 j+2가 되면 탐색 종료
                if cury1 == j+2:
                    break
                cury1 += 1

            # step2-1. 같은 x좌표의 우측에 격자 배치
            for a in range(j+3,n):
                cnt2 = 0
                # y좌표가 a+2까지 존재할 때에만 진행
                if in_range(i,a+2):
                    cury2 = a
                    while(1):
                        # 동전이 있으면 카운트
                        if arr[i][cury2] == 1:
                            cnt2 += 1
                        # 격자의 길이가 3이므로 y좌표가 a+2가 되면 탐색 종료
                        if cury2 == a+2:
                            break
                        cury2 += 1

                # 최댓값 갱신
                result = max(result,cnt+cnt2)

            # step2-2. 배열 아래로 내려가 격자 배치
            for k in range(i+1,n):
                for l in range(n):
                    cnt3 = 0
                    
                    # y좌표가 l+2 까지도 배열이 존재하면 탐색한다.
                    if in_range(k,l+2):
                        cury3 = l
                        
                        while(1):
                            # 동전이 존재할 때 카운트
                            if arr[k][cury3] == 1:
                                cnt3 += 1
                            # 격자의 길이가 3이므로 l+2까지만 탐색한다.
                            if cury3 == l+2:
                                break
                            cury3 += 1
                    # 결과값 갱신
                    result = max(result,cnt1+cnt3)

print(result)
'''