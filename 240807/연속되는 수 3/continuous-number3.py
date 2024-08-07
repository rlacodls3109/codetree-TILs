N = int(input())

arr = [
    int(input())
    for _ in range(N)
]

# 부호가 양수면 true, 음수면 false
sign_i_b = True
sign_i = True

cnt = 0
max_cnt = 0

for i in range(N):
    if arr[i] > 0:
        sign_i = True
    else :
        sign_i = False  
    if i == 0 or sign_i == sign_i_b:
        cnt += 1
    else :
        cnt = 1
    sign_i_b = sign_i
    max_cnt = max(max_cnt,cnt)

print(max_cnt)