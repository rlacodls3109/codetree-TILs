arr = input().split()
b,a = int(arr[0]), int(arr[1])

while b >= a:
    if b % 2 == 0 :
        print(b, end= " ")
    b -= 1