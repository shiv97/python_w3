x = input('enter 2 nos.:')
y = input()
if x > y:
    num = x
else:
    num = y
print('common divisors are:')
for i in range(1, num):
    if (x % i == 0 & y % i == 0):
        print(i)
