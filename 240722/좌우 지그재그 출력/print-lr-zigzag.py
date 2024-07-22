n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(n*(i+1)-(n-j-1),end=" ")
        else :
            print(n*(i+1)-j,end=" ")
    print()

#n*(i+1)-(n-j+1)
#n*(i+1)-j