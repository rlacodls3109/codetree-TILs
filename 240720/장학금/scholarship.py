k = input()
arr = k.split()
a, b = int(arr[0]), int(arr[1])

if a < 90:
    print(0)

elif b >= 95:
    print(100000)

elif b >= 90:
    print(50000)

else :
    print(0)