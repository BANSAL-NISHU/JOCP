"""
Leap years are years where an extra, or intercalary, day is added to the end of the shortest month, February.
The intercalary day, February 29, is commonly referred to as leap day.

Leap years have 366 days instead of the usual 365 days and occur almost every four years.

Most of the years that can be divided by 4 are leap years.
Exception: Century years are not leap years unless they are divided by 400.
"""

year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year.")

else:
    if year % 4 == 0:
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year.")