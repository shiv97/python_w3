import datetime
print('local time:')
print(datetime.datetime.now().time())
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)