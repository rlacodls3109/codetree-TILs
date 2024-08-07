N = int(input())

# 숫자를 입력받아 배열로 저장
arr = [
    int(input())
    for _ in range(N)
]

cnt = 0
max_cnt = 0 # 최대 횟수

for i in range(N):
    # 맨 처음 원소는 비교할 직전 원소가 없으므로 카운트
    # 직전 원소와 같다면 카운트
    if i == 0 or arr[i] == arr[i-1]:
        cnt += 1
    
    # 같지 않다면 다시 1부터 카운트
    else:
        cnt = 1
    
    #매 반복마다 최댓값을 갱신
    max_cnt = max(max_cnt,cnt)

print(max_cnt)