def draw_rectangle(n,m):
    for i in range(n):
        print("1"*m)

arr = input().split()
a,b = int(arr[0]), int(arr[1])

draw_rectangle(a,b)