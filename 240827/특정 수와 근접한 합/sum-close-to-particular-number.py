import sys

n, s = tuple(map(int,input().split()))
number_list = list(map(int,input().split()))

#최솟값을 시스템 최대 크기로 설정
result = sys.maxsize

# 입력받은 숫자의 합을 계산한다.
number_total = 0
for num in number_list:
    number_total += num

# 배열 순차 탐색
for i in range(n):
    for j in range(i+1,n):
        # 총 합에서 두 수를 뺀다
        cal = number_total - number_list[i] - number_list[j]
        # 결과값과 현재 계산 결과를 비교하여 작은 값을 갱신한다.
        result = min(result,abs(s - cal))

print(result)