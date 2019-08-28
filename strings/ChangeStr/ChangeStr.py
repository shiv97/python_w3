def change_sring(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]
stri=input('enter string')
print(change_sring(stri))
