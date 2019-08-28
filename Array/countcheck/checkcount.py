from array import *
array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))
n=int(input('enter the number to check occurance:'))
print("Number of occurrences: "+str(array_num.count(n)))