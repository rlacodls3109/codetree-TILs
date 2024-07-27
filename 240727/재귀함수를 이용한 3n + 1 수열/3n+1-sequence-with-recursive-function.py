'''
# 내정답 : a라느 count 변수를 안써도 return 값에 1을 하나씩 더하면 되는군!,,
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
'''

def count_number(a):
    if a == 1:
        return 0

    if a % 2 == 0:
        return count_number(a // 2) + 1
    else:
        return count_number(3 * a + 1) + 1

n = int(input())
print(count_number(n))