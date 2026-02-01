# A password should be considered as strong which follows :
# len >= 8
# At least 1 Lowercase letter 
# At least 1 Uppercase letter
# At least 1 Digit
# At least 1 Special Character

password = input("Enter your password:")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if len(password) < 8:
    print("Password must be at least 8 characters long")
else :
    for ch in password:
        if ch.isupper():
            has_upper = True

        if ch.islower():
            has_lower = True

        if ch.isdigit():
            has_digit = True

        if ch in special_chars:
            has_special = True


if has_upper and has_lower and has_digit and has_special:
    print("Strong Password ✅")
else:
    print("Weak Password ❌")