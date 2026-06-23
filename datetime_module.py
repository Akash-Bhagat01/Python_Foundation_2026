from datetime import datetime, date, time, timedelta

# 1. Current date & time
print(datetime.now())
# 2. Current date only
print(date.today())
# 3. Current time only
print(datetime.now().time())
# 4. Create custom date
d = date(2024, 12, 31)
print(d)

# 5. Create custom time
t = time(10, 30, 45)
print(t)

# 6. Format datetime
print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# 7. Add days
print(date.today() + timedelta(days=5))

# 8. Subtract days
print(date.today() - timedelta(days=10))

# 9. Difference between two dates
d1 = date(2025, 1, 1)
d2 = date.today()
print((d2 - d1).days)

# 10. Timestamp
print(datetime.now().timestamp())
