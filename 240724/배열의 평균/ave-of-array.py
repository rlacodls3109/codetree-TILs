arr=[
    list(map(int,input().split()))
    for _ in range(2)
]

for i in range(2):
    sum = 0
    for j in range(4):
        sum += arr[i][j]
    avg = sum/4
    print(f"{avg:.1f}",end =" ")
print()

for j in range(4):
    sum = 0
    for i in range(2):
        sum += arr[i][j]
    avg = sum / 2
    print(f"{avg:.1f}",end=" ")
print()

sum = 0
for i in range(2):
    for j in range(4):
        sum += arr[i][j]

avg = sum / 8
print(f"{avg:.1f}")