n = int(input())
digits = []
while(1):
    if n < 2:
        digits.append(n)
        break
    else:
        digits.append(n % 2)
        n //= 2
    

for digit in digits[::-1]:
    print(digit,end="")