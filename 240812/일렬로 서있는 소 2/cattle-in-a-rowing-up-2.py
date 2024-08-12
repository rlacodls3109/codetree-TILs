n = int(input())

cow_h = list(map(int,input().split()))

cnt = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            #A[i] ≤ A[j] ≤ A[k] 라면 개수 세기
            if cow_h[i] <= cow_h[j] and cow_h[j] <= cow_h[k]:
                cnt += 1

print(cnt)