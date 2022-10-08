def palindrome(num):
    before = num
    num = str(abs(before))
    res = ''.join(reversed(num))
    if before < 0:
        return -int(res)
    else:
        return int(res)

num = int(input())
print('Input: ', num)
print('Output: ', palindrome(num))