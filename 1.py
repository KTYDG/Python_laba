def palindrome(num):
    before = abs(int(num))
    num = str(before)
    res=''.join(reversed(num))
    if res == str(before):
        print('Это палиндром: ', before, '==', res)
    else:
        print('Это не палиндром: ', before, '=/=', res)

palindrome(100)
palindrome(101)
palindrome(202020202)
palindrome(666)
palindrome(1234)
