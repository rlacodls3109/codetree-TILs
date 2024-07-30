def same(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

word1 = input()
word2 = input()

arr1 = list(word1)
arr2 = list(word2)

arr1.sort()
arr2.sort()

if same(arr1,arr2):
    print("Yes")
else:
    print("No")