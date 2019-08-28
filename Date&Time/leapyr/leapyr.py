def leap_year(yr):
    if yr % 400 == 0:
        print('leap yr')
    if yr % 100 == 0:
        print('not a leap yr')
    if yr % 4 == 0:
        print('leap yr')
    else:
        print('not a leap yr')
print(leap_year(1998))