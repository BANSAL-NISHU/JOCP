"""
The birthday paradox, also known as the birthday problem, states that in a random group of 23 people,
there is about a 50% chance that two people have the same birthday.


A leap year is a calendar year containing one additional day added to keep the calendar year synchronized with the
astronomical or seasonal year. So during leap year, the February has 29 days instead of 28 days.
There are 366 days in a leap year.
There are 365 days in a non leap year.


January, March, May, July, August, October, December = 31 days.
April, June, September, November = 30 days.
If given year is a leap year then
              February has 29 days
else
              February has 28 days
"""

import random
import datetime
birthday = []


def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return 1
        else:
            return 0

    else:
        if year % 4 == 0:
            return 1
        else:
            return 0


i = 0
print("Randomly generated Dates of birth: ")
while i < 50:
    year = random.randint(1899, 2021)                 # the oldest person ever lived was 122 years old
    leap = leap_year(year)
    month = random.randint(1, 12)

    if month == 2 and leap == 1:
        day = random.randint(1, 29)
    elif month == 2 and leap == 0:
        day = random.randint(1, 28)
    elif month == 7 or month == 8:
        day = random.randint(1, 31)
    elif month % 2 != 0 and month < 7:
        day = random.randint(1, 31)
    elif month % 2 == 0 and 7 < month < 12:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)

    DOB = datetime.date(year, month, day)
    print(DOB)
    day_of_year = DOB.timetuple().tm_yday

    i = i + 1
    birthday.append(day_of_year)

birthday.sort()
i = 0
print("====================")
print("Day of year: ")
while i < 50:
    print(birthday[i], end="  ")
    i = i + 1
