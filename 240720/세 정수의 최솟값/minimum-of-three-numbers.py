k = input()
arr = k.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if a <= b and a<= c:
    print(a)

elif b<= c :
    print(b)

else :
    print(c)