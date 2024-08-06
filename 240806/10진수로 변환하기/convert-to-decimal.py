n = input()

# 입력받은 2진수를 거꾸로 뒤집은 배열을 만든다
arr = [
    digit
    for digit in n[::-1]
]

ten = 0

for i,digit in enumerate(arr):
    if digit == "1":
        ten = ten + 2 ** i

print(ten)