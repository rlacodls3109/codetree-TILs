n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print(0, end=" ")
    
    else:
        for j in range(len(str(i))):
            if str(i)[j] == "3" or str(i)[j] == "6" or str(i)[j] == "9":
                print(0, end=" ")
            else:
                print(i, end=" ")