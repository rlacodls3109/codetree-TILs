#a진수를 10진수로 바꾸는 함수
def a_to_ten(n,a):
    #주어진 a진수 n의 자리수를 구한다.
    n_length = len(n)
    
    ten = 0 # 변환된 10진수를 저장할 변수

        #n의 자릿수만큼 반복한다.
        for i in range(n_length):
            # 10진수 변환 방법 : 각각의 자리 숫자에 a의 자릿수(0부터 시작)제곱을 곱해서 결과에 더해준다.
            ten += (int(n[i]) * (a**(n_length-i-1)))
    return ten

#10진수를 b진수로 바꾸는 함수
def ten_to_b(n,b):
    result = ""

    while(1):
        if n < b:
            #마지막으로 n을 맨 앞에 추가한다.
            result = str(n) + result
            break
        else:
            # n%b의 결과를 맨 앞에 추가한 후, n 값 갱신
            result = str(n%b) + result
            n //= b
    
    return result

a, b = tuple(map(int,input().split()))
n = input()

#n을 10진수로 변환한 후, 그 값을 b진수로 변환한다.
ten = a_to_ten(n,a)
result = ten_to_b(ten,b)
print(result)