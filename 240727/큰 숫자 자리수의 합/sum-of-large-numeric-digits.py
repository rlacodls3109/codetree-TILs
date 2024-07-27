def answer(n):
    if n // 10 == 0:
        return n
    return answer(n//10) + (n % 10)

a,b,c= tuple(map(int,input().split()))

result = a*b*c
print(answer(result))