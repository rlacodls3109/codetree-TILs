N = int(input())

#숫자 입력받아 배열로 저장
arr = [
    int(input())
    for _ in range(N)
]

# 부호가 양수면 true, 음수면 false
sign_i_b = True # 직전 원소의 부호
sign_i = True # 현재 원소의 부호

cnt = 0
max_cnt = 0

for i in range(N):
    # 현재 원소의 부호 판별
    if arr[i] > 0:
        sign_i = True
    else :
        sign_i = False  
    
    # 맨 처음 원소는 비교 대상이 없으므로 카운트
    # 직전 원소의 부호와 현재 원소의 부호가 같으면 카운트
    if i == 0 or sign_i == sign_i_b:
        cnt += 1

    #아니면 1부터 카운트 시작
    else :
        cnt = 1
    
    #다음 반복 전에 sign_i_b를 갱신
    sign_i_b = sign_i
    #매 반복마다 max값 갱신
    max_cnt = max(max_cnt,cnt)

print(max_cnt)