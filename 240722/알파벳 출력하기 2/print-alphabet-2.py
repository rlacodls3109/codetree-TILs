n = int(input())
char= int(ord('A'))

for i in range(n):
    for j in range(n):
        if i>j:
            print(" ",end=" ")
        else:
            print(chr(char), end=" ")
            char += 1
            if char == int(ord('Z')) + 1:
                char = int(ord('A'))
    print()