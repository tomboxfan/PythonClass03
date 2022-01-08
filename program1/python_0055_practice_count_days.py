'''
Requirement:
user inputs year / month / day information from the console
Your program needs to tell the user how many days in the year there are in front of the date which user input
For example: if user tells you 2019 Jan 1st, then your output should be 1
For example: if user tells you 2019 Feb 1st, then your output should be 32
HINT: Please consider leap year.
'''


# define the variable ----------------------------

year = int(input("Please input year:"))
month = int(input("Please input month:"))
day = int(input("Please input day:"))

print(year, "-", month, "-", day)

total_days = 0

# use the variable -----------------------------

# handle the month

if month > 1:
    total_days += 31
if month > 2:
    total_days += 28
if month > 3:
    total_days += 31
if month > 4:
    total_days += 30
if month > 5:
    total_days += 31
if month > 6:
    total_days += 30
if month > 7:
    total_days += 31
if month > 8:
    total_days += 31
if month > 9:
    total_days += 30
if month > 10:
    total_days += 31
if month > 11:
    total_days += 30


# handle the day

total_days += day

# handle the leap year

is_leap_year = False

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    is_leap_year = True

if is_leap_year and month > 2:
    total_days +=1

print("Total days:", total_days)

