k = input()
arr = k.split()
a_m, a_e = int(arr[0]), int(arr[1])

j = input()
arr2 = j.split()
b_m,b_e = int(arr2[0]), int(arr2[1])

if a_m == b_m:
    print("A" if a_e > b_e else "B")

else :
    print("A" if a_m > b_m else "B")