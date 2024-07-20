arr = input().split()

a,b = int(arr[0]), int(arr[1])

print(a//b, end="")
print(".",end="")

rest = a%b

for i in range(20):
    print((rest * 10) // b,end="")
    rest = (rest*10) % b