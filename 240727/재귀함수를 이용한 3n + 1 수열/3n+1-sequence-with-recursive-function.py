a = 0 

def answer(n):
    global a
    if n == 1:
        return
    a += 1
    if n % 2 == 0:
        answer(n//2)
    else :
        answer((n*3)+1)


n = int(input())
answer(n)
print(a)