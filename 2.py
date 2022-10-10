def div_lists(li):
    l2 = [num for num in li if num % 2 == 0]
    l3 = [num for num in li if num % 3 == 0]
    l5 = [num for num in li if num % 5 == 0]
    print('On 2: ', l2)
    print('On 3: ', l3)
    print('On 5: ', l5)

# list = list(map(int, input().split()))
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

div_lists(test)

