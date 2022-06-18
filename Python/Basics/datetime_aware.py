import datetime
import pytz

# Assigning an aware datetime (with timezone and microsecond=0)
dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

# Current UTC time
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# Unusual way to get current UTC time
dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow2)

# Print all timezone to know 'Asia/Dubai'
# for tz in pytz.all_timezones:
#     print(tz)

# Get Dubai time with timezone
dt_uae = dt_utcnow.astimezone(pytz.timezone('Asia/Dubai'))
print(dt_uae)

# Get Dubai time without timezone and then assign timezone offset
dt_uae = datetime.datetime.now()
print(dt_uae)
uae_tz = pytz.timezone('Asia/Dubai')
print(type(uae_tz))
dt_uae = uae_tz.localize(dt_uae)
print(dt_uae)

# Convert Dubai time to Indian time using astimzone function
dt_ind = dt_uae.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_ind)

# strftime - datetime to string
print(dt_uae.strftime('%B %d, %Y'))

# ISO format date/time
print(dt_uae.isoformat())
print(type(dt_uae.isoformat()))

# strptime - string to datetime object
DT_STR = 'July 24, 2016'
dt = datetime.datetime.strptime(DT_STR, '%B %d, %Y')
print(dt)
print(type(dt))
