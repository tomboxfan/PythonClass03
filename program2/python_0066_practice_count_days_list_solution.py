
year = int(input("Please input year:"))
month = int(input("Please input month:"))
day = int(input("Please input day:"))

dayList = []

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