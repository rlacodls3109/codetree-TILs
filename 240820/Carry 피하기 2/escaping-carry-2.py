import sys

MAX_INT = - sys.maxsize

# carry가 발생했는 지 구하는 함수
def not_carry(a,b,c):
    if a+b+c >= 10:
        return False
    else:
        return True

# 숫자를 각 자리 별로 자르는 함수
def slice_num(number):
    result = []
    for i in range(4):
        result.append(number % 10)
        number //= 10
    return result

n = int(input())

num_list = [
    int(input())
    for _ in range(n)
]

# 정답이 없으면 -1
ans = -1

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            # 숫자 세개를 선택
            num1 = slice_num(num_list[i])
            num2 = slice_num(num_list[j])
            num3 = slice_num(num_list[k])
            # carry가 발생하지 않는다면 숫자를 더한다
            if not_carry(num1[0],num2[0],num3[0]) and not_carry(num1[1],num2[1],num3[1]) and not_carry(num1[2],num2[2],num3[2]) and not_carry(num1[3],num2[3],num3[3]):
                cal = num_list[i] + num_list[j] + num_list[k]
                ans = max(ans,cal)

print(ans)