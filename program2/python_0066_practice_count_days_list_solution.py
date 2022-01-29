
year = int(input("Please input year:"))
month = int(input("Please input month:"))
day = int(input("Please input day:"))

dayList = [0,    # There are 0 days in those full months in front of any Jan date.
           31,   # There are 31 days in those full months in front of any Feb date.
           31 + 28,   # There are 31 + 28 days in those full months in front of any Mar date.
           31 + 28 + 31,   # Apr
           31 + 28 + 31 + 30,   # May
           31 + 28 + 31 + 30 + 31,   # Jun
           31 + 28 + 31 + 30 + 31 + 30,   # Jul
           31 + 28 + 31 + 30 + 31 + 30 + 31,   # Aug
           31 + 28 + 31 + 30 + 31 + 30 + 31 + 31,   # Sep
           31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30,   # Oct
           31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31,   # Nov
           31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30   # Dec
]

totalDays = dayList[month-1] #list index starts from 0, so minus 1

totalDays += day

# check leap year ------------------------------------------------------
leapYear = False

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leapYear = True

if leapYear and month > 2:
    totalDays += 1

# ----------------------------------------------------------------------

print("Total days: ", totalDays)