def palindrome(teststr):
    if len(teststr) <= 1:
        return True
    elif teststr[0] == teststr[-1]:
        return palindrome(teststr[1:-1])
    else :
        return False

strA = "{[(p)]}"
print(palindrome(strA))