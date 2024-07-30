class Sales:
    def __init__(self,name="codetree",code=50):
        self.name = name
        self.code = code
    
sales1 = Sales()
print("product", sales1.code,"is",sales1.name)

a, b = tuple(input().split())
b = int(b)
sales1.name = a
sales1.code = b

print("product", sales1.code,"is",sales1.name)