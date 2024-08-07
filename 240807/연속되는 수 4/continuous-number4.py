N = int(input())

#숫자 입력받아 배열로 저장
arr = [
    int(input())
    for _ in range(N)
]

cnt = 0
max_cnt = 0


for i in range(N):
    # 맨 처음 원소는 비교대상 없으므로 카운트
    # 직전 원소보다 크다면 카운트
    if i == 0 or arr[i] > arr[i-1]:
        cnt += 1
    
    # 아니면 카운트 1부터 다시 시작
    else:
        cnt = 1
    
    # 매 반복마다 max값 갱신
    max_cnt = max(cnt,max_cnt)

print(max_cnt)