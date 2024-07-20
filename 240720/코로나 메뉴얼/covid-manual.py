k= input()
arr = k.split()
cold_a= arr[0]
them_a= int(arr[1])

k= input()
arr = k.split()
cold_b= arr[0]
them_b= int(arr[1])

k= input()
arr = k.split()
cold_c= arr[0]
them_c= int(arr[1])

if cold_a == "Y" and them_a >=37:
    if (cold_b =="Y" and them_b >= 37) or (cold_c =="Y" and them_c >= 37):
        print("E")
    else :
        print("N")

else:
    if (cold_b =="Y" and them_b >= 37) and (cold_c =="Y" and them_c >= 37):
        print("E")
    else :
        print("N")