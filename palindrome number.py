def is_palindrome(num):
    # Convert number to string and compare with its reverse
    return str(num) == str(num)[::-1]

# Test the function
num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
