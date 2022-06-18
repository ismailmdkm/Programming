import datetime

# creating instance of class 'datetime.date'
d = datetime.date(2022, 4, 22) 
print(d)
print(type(d))

# today method to get current date
today = datetime.date.today()  
print(today)
print(today.year)
print(today.day)
print(today.month)
print(type(today))
print(type(today.year))

# day of week
# Monday is 0
print(today.weekday())  
# Monday is 1 on ISO
print(today.isoweekday())

# Time deltas - difference between two dates
tdelta = datetime.timedelta(days=7)
print(today)
print(tdelta)
print(today + tdelta)
print(today - tdelta)
print(type(tdelta))
print("*"*20)

# date2 = date1 +/- timedelta
# timedelta = date1 +/- date2
bday = datetime.date(2022, 5, 20)
till_bday = bday - today
print(till_bday)
print(type(till_bday))
print(till_bday.days)
print(till_bday.total_seconds())

# TIME
print("*"*50)
t = datetime.time(9, 30, 45, 1089)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print(type(t))
print(type(t.hour))

# DATE and TIME
dt = datetime.datetime(2022, 4, 22, 12, 30, 45, 18391)
print(dt)
print(dt.date())
print(dt.time())
print(type(dt))
print(type(dt.date()))
print(type(dt.time()))
print(dt.year)
print(dt + tdelta)
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)
print('-'*30)

import pytz
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_nowtz = datetime.datetime.now(tz=pytz.utc)
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_nowtz)
print(dt_utcnow)
print(type(dt_today))
print(type(dt_now))
print(type(dt_nowtz))
print(type(dt_utcnow))



# # Timezone aware
# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.utc)
# print(dt)

# dt_utcnow = datetime.datetime.now(tz=pytz.utc)
# print(dt_utcnow)
