# Powerautomate- Github PR Approval Notification flow
def is_palindrome(num):
    original = str(num)
    reverse = original[::-1]

    return original == reverse


number = 121

if is_palindrome(number):
    print(number, "is a Palindrome")
else:
    print(number, "is not a Palindrome")