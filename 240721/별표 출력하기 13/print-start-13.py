#홀수번째는 1씩감소 짝수번째는 1씩 증가

n = int(input())

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
    for k in range(i+1):
        print("*",end=" ")
    print()