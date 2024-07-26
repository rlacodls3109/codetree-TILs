def answer(n):
    global cnt
    if n == 1:
        return 0
    if n % 2 == 0:
        return answer(n//2) + 1
    
    else:
        return answer(n//3) + 1
     

n = int(input())
print(answer(n))