'''
Requirement:
Implement a phone/address book program using dictionary.
The dictionary uses person names as keys.
Each person is represented as another dictionary with the keys 'phone' and 'addr' referring to their phone number and address respectively.


        phone   home address
Alice:  2341    Foo drive 23
Beth:   9102    Bar street 42
Cecil:  3158    Baz avenue 90
'''

'''
The phone number and home address behind user name is also another dict
'''

alice_dict = {
    'phone': '2341',
    'address' : 'Foo drive 23'
}

beth_dict = {
    'phone': '9102',
    'address' : 'Bar street 42'
}

cecil_dict = {
    'phone': '3158',
    'address' : 'Baz avenue 90'
}

people_dict = {
    'Alice' : alice_dict,
    'Beth' : beth_dict,
    'Cecil' : cecil_dict
}

# print(f"LOG - people dict is: {people_dict}")

'''
We can open the dict directly in website: http://jsonviewer.stack.hu/
'''

# TEST CODE -------------------------------------------

name = input("Name (Alice / Beth / Cecil): ")

if name not in people_dict:
    print(f"No such person: {name}, program exit!")
    exit()

info_dict = people_dict[name]

# print(f"LOG - {name} info dict is: {info_dict}")

request = input("'Phone number' (p) or 'Address' (a): ")

if request == 'p':
    key = 'phone'
elif request == 'a':
    key = 'address'
else:
    print(f"Unrecognized request: {request}, program exit!")
    exit()

print(f"{name}'s {key} is: {info_dict[key]}")

'''
HOMEWORK: How to modify the program to let the program run continuously? 
'''