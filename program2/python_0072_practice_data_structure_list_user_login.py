
'''
Requirement:
Simulate a user login process

Answer is far below...
'''

























# PREPARE DATA BEGIN --------------------------

database = [
    ['albert', '1234'],
    ['smith', '4242'],
    ['Jiexi', '7542'],
    ['BingXuan', '5674']
]

username = input("Username:")
pin = input("Password:")

# MAIN PROGRAM BEGIN --------------------------

if [username, pin] in database:
    print("Access granted!")
else:
    print("Wrong user/pass combinations!")


