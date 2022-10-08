def palindrome(num):
    before = abs(int(num))
    num = str(before)
    res=''.join(reversed(num))
    if res == str(before):
        return True
    else:
        return False

if palindrome(input()):
    print('Это палиндром')
else:
    print('Это не палиндром')
