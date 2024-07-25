def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def mult(a,b):
    return a*b
def divide(a,b):
    return a//b

a,o,c = tuple(input().split())
a,c = int(a), int(c)
if o == '+':
    print(a,o,c,"=",plus(a,c))
elif o == '-':
    print(a,o,c,"=",minus(a,c))
elif o == '*':
    print(a,o,c,"=",mult(a,c))
elif o == '/':
    print(a,o,c,"=",divide(a,c))
else:
    print("False")