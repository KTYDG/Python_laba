import functools


def caching(func):
    def wrapper(arg1, arg2):
        cache_key = arg1
        if cache_key not in wrapper.cache:
            print('\n#####\nхехе, я закэшировался')
            wrapper.cache[cache_key] = func(arg1, arg2)
            print('\nхихи, а я теперь кэширован\n')
        else:
            print('\n#####\nхехе, а я уже кэширован\n')
        res = []
        for i in range(0, arg2):
            print('хаха, я вставляю результаты')
            res.append(str(wrapper.cache[cache_key]))
        print('\nхихихаха, я закэшировался снова\n#####\n')
        wrapper.cache[cache_key] = func(arg1, arg2)
        return res
    wrapper.cache = dict()
    return wrapper

@caching
def prime(num, cache_amount):
    if num == 0 or num > 100000:
        print(num, '? Ты зачем так делаешь?')
    elif num == 1:
        return True
    else:
        for i in range(2, 100000):
            if i != num and num % i == 0:
                return False
            elif i > num:
                return True

num = 17  # int(input())
cache = 5 # int(input())
# print(prime(num, cache))
# print(prime(num, cache))
# print(prime(num, cache))

for statement in prime(num, cache):
    if statement == str(True):
        print("Простое число")
    else:
        print("Не простое число")


