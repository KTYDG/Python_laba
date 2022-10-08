list = list(map(int, input().split()))

l2 = []
l3 = []
l5 = []

for num in list:
    if num%2==0:
        l2.append(num)
    if num%3==0:
        l3.append(num)
    if num%5==0:
        l5.append(num)

print(l2)
print(l3)
print(l5)