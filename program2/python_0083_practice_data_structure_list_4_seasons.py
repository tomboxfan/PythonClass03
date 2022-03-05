# You are given 4 seasons list as below
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]

# You need to ask user to input a number between 1 - 12
# Then you tell the user which season it belongs to.

month = int(input("month: "))

if month in spring:
    print("It is spring season")
elif month in summer:
    print("It is summer season")
elif month in autumn:
    print("It is autumn season")
elif month in winter:
    print("It is winter season")
else:
    print("Please give me a valid month")

