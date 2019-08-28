def string_reverse(str):
    rr1 = ''
    index = len(str)
    while index > 0:
        rr1 += str[ index - 1 ]
        index = index - 1
    return rr1
n=input('enter string')
print(string_reverse(n))