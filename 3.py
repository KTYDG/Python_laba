def palindrome(num):
    before = num
    num = str(abs(before))
    res = int(''.join(reversed(num)))
    if before < 0:
        res = -res
    print('\nInput: ', before)
    print('Output:', res)

palindrome(123)
palindrome(-359)
palindrome(120)
palindrome(2040)