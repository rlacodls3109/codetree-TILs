arr = [0] * 201

n = int(input())

current_point = 100
for _ in range(n):
    a, b = tuple(input().split())
    a = int(a)

    if b == 'R':
        for i in range(current_point,current_point+a):
            arr[i] += 1
        current_point += a
    
    elif b == 'L':
        for i in range(current_point - a,current_point):
            arr[i] += 1
        current_point -= a

cnt = 0
for elem in arr:
    if elem >= 2:
        cnt += 1

print(cnt)