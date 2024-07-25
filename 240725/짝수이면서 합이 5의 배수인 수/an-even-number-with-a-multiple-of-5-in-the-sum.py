def is_magic_num(n):
    a = n // 10
    b = n % 10 
    return n % 2 == 0 and (a+b) % 5 == 0

n = int(input())
if is_magic_num(n):
    print("Yes")
else:
    print("No")