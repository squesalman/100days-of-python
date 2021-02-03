#%%
from datetime import datetime
from datetime import date
from datetime import timedelta


today_datetime = datetime.today()
today_date = datetime.date(today)
time_delta = timedelta(hours=6,days=5)

print(today_datetime)
print(today_date)
print(time_delta)

time_delta.days
time_delta.seconds

delta = timedelta(days=50,seconds=27,microseconds=10,milliseconds=29000,minutes=5,hours=8,weeks=2)

newdelta = today_datetime - delta
print(newdelta)
delta

# %%
from datetime import date
from datetime import datetime

datetime.today()
today = datetime.today()
print(f'time is : {today}')
print(f'Type of the object today : {type(today)}')

todaydate = date.today()
print(f'Date is : {todaydate}')
print(f'Type of the object todaydate : {type(todaydate)}')
print(f'Month : {todaydate.month}')
print(f'Year : {todaydate.year}')
print(f'Day : {todaydate.day}')

christmas = date(2021,12,25)
christmas

if christmas is not todaydate:
  print(f'Sorry there are still {str((christmas - todaydate).days)} until christmas !')
else:
  print("Yay its Christmas!")

if christmas is not todaydate:
  print(f'Sorry there are still {(christmas - todaydate).days} days until christmas !')
else:
  print("Yay its Christmas!")


# %%
from datetime import datetime
from datetime import date

test_date = date.today()
test_date
str(test_date)
# %%
from datetime import timedelta
from datetime import date
from datetime import datetime

t = timedelta(days=4, hours=10)

t.days
t.seconds
t.seconds / 60 / 60
t.seconds / 3600

eta = timedelta(hours=6)

today = datetime.today()

today

today + eta

str(today+eta)
# %%
