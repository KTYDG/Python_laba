def prime(num):
    if num == 0 or num > 100000:
        print('Ты дурак?')
    elif num == 1:
        return True
    else:
        for i in range(2, 100000):
            if i != num and num%i == 0:
                return False
            elif i > num:
                return True

if prime(int(input())):
    print("Простое")
else:
    print("Не простое")
