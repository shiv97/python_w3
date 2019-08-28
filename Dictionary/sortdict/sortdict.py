import operator
d= {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(0),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)