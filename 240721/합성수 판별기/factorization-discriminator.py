n = int(input())
result = 'N'
for i in range(2,n):
    if n % i == 0:
        result = 'C'

print(result)