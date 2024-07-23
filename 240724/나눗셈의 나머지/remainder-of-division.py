rest = [0 for i in range(10)]

arr = list(map(int,input().split()))
a,b = arr[0],arr[1]

while(1):
    a = a/b
    rest[int(a%b)] += 1
    if a <= 1:
        break

sum = 0

for i in rest:
    sum += i*i

print(sum)