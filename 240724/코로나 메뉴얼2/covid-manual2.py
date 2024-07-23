hos = [0 for i in range(4)]

for i in range(3):
    a, b = input().split()
    b = int(b)

    if a == 'Y' and b >= 37:
        hos[0] += 1
    elif a=='N' and b >= 37:
        hos[1] += 1
    elif a=='Y' and b < 37:
        hos[2] += 1
    else:
        hos[3] += 1


for i in hos:
    print(i,end=" ")

if hos[0] >=2:
    print('E',end=" ")