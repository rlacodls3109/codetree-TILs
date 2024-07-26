def answer(a,b):
    if a > b :
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    return a,b

a, b = tuple(map(int,input().split()))

a, b = answer(a,b)
print(a,b)