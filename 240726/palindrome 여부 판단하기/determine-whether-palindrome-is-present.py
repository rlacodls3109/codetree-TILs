def is_palindrome(string):
    a = string[-1::-1]
    if string == a:
        return True
    return False

string = input()
if is_palindrome(string):
    print("Yes")
else:
    print("No")