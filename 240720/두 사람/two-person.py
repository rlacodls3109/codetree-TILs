k = input()
arr = k.split()
a_age, a_gender = int(arr[0]), arr[1]

j = input()
arr2 = j.split()
b_age, b_gender = int(arr2[0]), arr2[1]

if (a_age >= 19 and a_gender == "M") or (b_age >= 19 and b_gender =="M"):
    print(1)

else : 
    print(0)