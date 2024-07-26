cnt = 0

def answer(n):
    global cnt
    if n == 1:
        return
    cnt += 1
    if n % 2 == 0:
        return answer(n//2)
    
    else:
        return answer(n//3)
    

n = int(input())
answer(n)
print(cnt)