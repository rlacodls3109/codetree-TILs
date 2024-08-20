import sys

MAX_INT = -sys.maxsize

a = input()

# 입력받은 문자열 리스트로 저장
two_list = [
    i
    for i in a
]

max = MAX_INT


for i,binary in enumerate(two_list):
    #한 숫자를 바꾼 a를 저장할 리스트 b
    b = []
    for j in two_list:
        b.append(j)
    
    # i번째 자리 2진수가 0이면 1로, 1이면 0으로 바꾼다 
    b[i] = '0' if binary=='1' else '1'
    # 정수 N 구하기
    N = 0
    for index,two in enumerate(b) :
        if two == '1':
            N += 2 ** (len(b) - index-1)
    # 구한 정수 N이 최댓값인지 확인
    if max < N:
        max = N

print(max)