def Char_Occur(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n]=1
    return dict
str=input('enter a string:')
print(Char_Occur(str))