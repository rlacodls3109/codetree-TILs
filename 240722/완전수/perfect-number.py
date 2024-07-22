arr = input().split()
start, end = int(arr[0]), int(arr[1])
total = 0

for i in range(start, end+1):
    sum = 0    
    for j in range(1,i+1):
        if i % j == 0 and j != i:
            sum += j
    
    if i == sum:
        total += 1

print(total)