# 코드 줄이기!!!!!!!!
'''
n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

result = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        if in_range(i,j+1) and in_range(i,j+2):
            cury1 = j
            while(1):
                if arr[i][cury1] == 1:
                    cnt += 1
                if cury1 == j+2:
                    break
                cury1 += 1

            for a in range(j+3,n):
                cnt2 = 0
                if in_range(i,a+2):
                    cury3 = a
                    while(1):
                        if arr[i][cury3] == 1:
                            cnt2 += 1
                        if cury3 == a+2:
                            break
                        cury3 += 1

                result = max(result,cnt+cnt2)

            for k in range(i+1,n):
                for l in range(n):
                    cnt3 = 0
                    if in_range(k,l+1) and in_range(k,l+2):
                        cury2 = l
                        
                        while(1):
                            if arr[k][cury2] == 1:
                                cnt3 += 1
                            if cury2 == l+2:
                                break
                            cury2 += 1

                    result = max(result,cnt+cnt3)

print(result)
'''

# 변수 선언 및 입력
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# Step 1.
# 첫 번째 격자를 놓습니다. (i , j)
max_cnt = 0
for i in range(n):
    # 격자를 벗어나지 않을 범위로만 잡습니다.
    for j in range(n - 2):
        # 두 번째 격자를 놓습니다. (k , l)
        for k in range(n):
            # 격자를 벗어나지 않을 범위로만 잡습니다.
            for l in range(n - 2):
                # Step2. 두 격자가 겹치는 경우에는 가짓수로 세지 않습니다.
                if i == k and abs(j - l) <= 2:
                        continue
                
                # Step 3. 두 격자가 겹치지 않는 경우에 대해 동전 수를 세어 갱신해줍니다.
                cnt1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                cnt2 = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)