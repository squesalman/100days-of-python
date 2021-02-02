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

