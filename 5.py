def prime(num):
    if num == 0 or num > 100000:
        print(num, '? Ты зачем так делаешь?')
    elif num == 1:
        print(num, ' - простое')
    else:
        for i in range(2, 100000):
            if i != num and num%i == 0:
                print(num, '- не простое')
                break
            elif i > num:
                print(num, '- простое')
                break

prime(1)
prime(2)
prime(4)
prime(997)
prime(15)
prime(17)
prime(0)
prime(100001)