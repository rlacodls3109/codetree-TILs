def have_369(n):
    while(1):
        if n % 10 == 3 or n % 10 ==6 or n % 10 == 9:
            return True
        else:
            n = n // 10
        if n == 0:
            return False

def is_magic_num(n):
    return n % 3 == 0 or have_369(n)

a,b = tuple(map(int,input().split()))

cnt = 0

for i in range(a,b+1):
    if is_magic_num(i):
        cnt += 1

print(cnt)