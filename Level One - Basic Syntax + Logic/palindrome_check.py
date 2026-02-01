def check_palindrome(s):
    s = s.replace(" ", "")
    rev = ""

    for ch in s:
        rev = ch + rev

    return rev == s
    
s = input("Enter String :").lower()

if check_palindrome(s) :
    print("Palindrome")

else :
    print("Not Palindrome")