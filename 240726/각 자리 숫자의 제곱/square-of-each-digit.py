def answer(n):
    if n < 10 :
        return n*n
    
    return answer(n // 10) + ((n % 10) ** 2)

n = int(input())
print(answer(n))