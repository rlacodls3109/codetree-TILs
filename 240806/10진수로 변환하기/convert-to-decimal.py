n = input()

# 입력받은 2진수를 거꾸로 뒤집은 배열을 만든다
arr = [
    digit
    for digit in n[::-1]
]

ten = 0

# 2진수가 1일때에만 2의 i제곱을 더해주는 방식으로 구현
# i 는 오른쪽부터 왼쪽으로 0부터 증가한다. 
for i,digit in enumerate(arr):
    if digit == "1":
        ten = ten + 2 ** i

print(ten)