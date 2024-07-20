sum = 0
cnt = 0
while True:
    age = int(input())

    if age >= 20 and age < 30:
        sum += age
        cnt += 1
    else :
        break

avg = sum / cnt
print(f"{avg:.2f}")