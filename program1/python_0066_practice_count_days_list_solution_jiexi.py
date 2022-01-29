year = int(input("Please input year:"))
month = int(input("Please input month:"))
day = int(input("Please input day:"))

dayList = [31,28,31,30,31,30,31,31,30,31,30,31]

totalDays=0

for i in range(0,month-1):
    totalDays += dayList[i]

totalDays += day

# check leap year ------------------------------------------------------
leapYear = False

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leapYear = True

if leapYear and month > 2:
    totalDays += 1

# ----------------------------------------------------------------------

print("Total days: ", totalDays)