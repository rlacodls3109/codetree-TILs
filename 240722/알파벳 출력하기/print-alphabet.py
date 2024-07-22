n = int(input())
char = int(ord('A'))
for i in range(n):
    for j in range(i+1):
        print(chr(char),end="")
        char += 1
        if chr(char) == 'Z':
            char = int(ord('A'))
    print()