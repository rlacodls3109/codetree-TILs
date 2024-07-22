n = int(input())

for i in range(1,n+1):
    result = True

    for j in range(1,i+1):
        if i == 1:
            result = False
            break
        if i % j == 0 and j != 1 and j != i:
            result = False
            break
    if result == True:
        print(i, end= " ")