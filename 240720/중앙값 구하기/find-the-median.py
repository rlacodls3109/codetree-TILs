arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

if a > b and a > c :
    if b > c :
        print(b)
    else :
        print(c)

elif a < b:
    if a > c:
        print(a)
    else: 
        print(c)

elif a < c:
    if a > b:
        print(a)
    else:
        print(b)