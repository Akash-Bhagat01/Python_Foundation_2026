# =====================================================
# PYTHON DATETIME & MATH MODULE EXAMPLES (FIXED)
# =====================================================

from datetime import datetime, date, time, timedelta
import math

# -----------------------------------------------------
# DATETIME MODULE
# -----------------------------------------------------

# 1. CURRENT DATE AND TIME
now = datetime.now()
print("Current Date & Time:", now)

# 2. CURRENT DATE ONLY
today = date.today()
print("Today's Date:", today)

# 3. CREATE CUSTOM DATE
custom_date = date(2025, 1, 1)
print("Custom Date:", custom_date)

# 4. CREATE CUSTOM TIME
custom_time = time(10, 30, 15)
print("Custom Time:", custom_time)

# 5. FORMAT DATE (strftime)
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date:", formatted_date)

# 6. STRING TO DATE (strptime)
date_string = "15-08-2024"
converted_date = datetime.strptime(date_string, "%d-%m-%Y")
print("Converted Date:", converted_date)

# 7. DATE DIFFERENCE (timedelta)
date1 = date(2024, 1, 1)
date2 = date(2024, 1, 10)
difference = date2 - date1
print("Date Difference:", difference.days, "days")

# 8. ADD DAYS TO DATE
future_date = today + timedelta(days=10)
print("Future Date:", future_date)

# -----------------------------------------------------
# MATH MODULE
# -----------------------------------------------------

# 9. SQUARE ROOT
print("Square Root:", math.sqrt(25))

# 10. POWER
print("Power:", math.pow(2, 3))

# 11. CEIL AND FLOOR
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.7))

# 12. FACTORIAL
print("Factorial:", math.factorial(5))

# 13. PI AND E CONSTANT
print("PI:", math.pi)
print("E:", math.e)

# 14. TRIGONOMETRY
angle = math.radians(30)
print("Sin 30:", math.sin(angle))
print("Cos 30:", math.cos(angle))

# 15. LOGARITHM
print("Log base 10:", math.log10(100))

# 16. ABSOLUTE VALUE
print("Absolute:", math.fabs(-15))

print("=== END OF DATETIME & MATH MODULE ===")
