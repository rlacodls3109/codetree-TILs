arr = [
    list(input().split())
    for _ in range(5)
]

for array in arr:
    for i in range(3):
        result = ord(array[i]) - (ord('a')-ord('A'))
        print(chr(result), end=" ")
    print()