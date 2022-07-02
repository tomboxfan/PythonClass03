from datetime import date, datetime

print("1) get today's date ------------------------")
today = date.today()
print(today)


print("2) get date & time (right now) -------------")
now = datetime.now()
print(now)


print("3) get hour / minute / second from 'now' ----------")
print(now.hour, now.minute, now.second)
print(f"{now.hour}:{now.minute}:{now.second}")

print("variable now.hour is of type: ", type(now.hour))




'''
HOMEWORK:
print current time to the turtle console
'''