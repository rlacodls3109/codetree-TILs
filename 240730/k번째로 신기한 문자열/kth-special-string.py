n, k, T = tuple(input().split())
n, k = int(n), int(k)

def compare(word,T):
    for i in range(len(T)):
        if word[i] != T[i]:
            return False
    return True
word_list=[
    input()
    for _ in range(n)
]

arr = []
for elem in word_list:
    if compare(elem,T):
        arr.append(elem)

arr.sort()
print(arr[k-1])