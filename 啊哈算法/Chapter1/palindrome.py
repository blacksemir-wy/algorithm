def palindrome(teststr):
    if len(teststr) <= 1:
        return True
    else:
        return palindrome(teststr[1:-1]) if teststr[0] == teststr[-1] else False


strA = "abcba"
print(palindrome(strA))
