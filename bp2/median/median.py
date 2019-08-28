x = input("enter 3 numbers:")
y = input(" ")
z = input(" ")
print("the median is")
if y < x < z:
    print(x)
elif z < x < y:
    print(x)
elif z < y < x:
    print(y)
elif x < y < z:
    print(y)
elif y < z < x:
    print(z)
elif x < z < y:
    print(z)
