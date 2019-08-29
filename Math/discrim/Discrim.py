def discriminant():
    a = float(input('The a value: '))
    b = float(input('The b value: '))
    c = float(input('The c value: '))
    discriminant = (b**2) - (4*a*c)
    if discriminant > 0:
        print('Two Solutions. Discriminant value is:', discriminant)
    elif discriminant == 0:
        print('One Solution. Discriminant value is:', discriminant)
    elif discriminant < 0:
        print('No Real Solutions. Discriminant value is:', discriminant)

discriminant()