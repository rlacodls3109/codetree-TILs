k = input()
arr = k.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

min = int(arr[0])
for i in arr:
    if min > int(i):
        min = int(i)
if a == min:
    print(1, end = " ")
else :
    print(0, end = " ")

if a == b and b == c:
    print(1)

else:
    print(0)