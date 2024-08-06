# 10진수를 2진수로 바꾸는 함수
def ten_to_bin(N):
    result = ""
    while(1):
        if N < 2:
            #마지막에는 N을 맨 앞에 추가한다.
            result = str(N) + result
            break
        else:
            # N%2 값을 맨 앞에 추가한다.
            result = str(N%2) + result
            N //= 2
    return result

#2진수를 10진수로 바꾸는 함수
def bin_to_ten(N):
    binary = []
    ten = 0

    #2진수를 거꾸로 뒤집은 결과를 binary라는 배열에 저장한다.
    for i in N[::-1]:
        binary.append(i)
    
    #2진수 자리가 1일 때, 2의 i제곱을 결과값에 더한다.
    for i,digit in enumerate(binary):
        if digit == "1":
            ten = ten + (2**i)
    return ten

#2진수는 문자열형태로 처리, 10진수는 정수형태로 처리한다.
N = input()

#입력받은 2진수(string)를 10진수로 변환
ten = bin_to_ten(N)

#17배
ten *= 17

#10진수를 2진수로 변환
result = ten_to_bin(ten)

print(result)