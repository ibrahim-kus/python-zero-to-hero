#import datetime
# from datetime import date
# from datetime import time
from datetime import datetime
from datetime import timedelta

result = dir(datetime)
res2 = datetime.now()
now = datetime.now()

res3 = now.month
res3 = datetime.strftime(now, '%A')

print(res2)
print(res3)

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

print(result)
print("****************")

birtday = datetime(1987,2,1,12,30,56)
result = datetime.timestamp(birtday) # convert saniye
result2 = datetime.fromtimestamp(result) # saniye to datetime
print(result)
print(result2)

result = now - birtday #timedelta

result = now + timedelta(days=10)
print(result)