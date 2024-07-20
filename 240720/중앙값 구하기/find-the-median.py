arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if a > b and a > c :
    if b > c :
        print(b)
    else :
        print(c)

elif a > b or a > c:
    print(a)

else:
    if b > c:
        print(c)
    else:
        print(b)