'''
There is big resort, it has 2000 rooms.
Door number tiles need to be installed for all these 2000 rooms, starting from '0001' to '2000'.
Door number is composed of 4 tiles. i.e.
'0001' is composed of 3 '0' and 1 '1';
'2000' is composed of 3 '0' and 1 '2'.

Question:
How many tiles need to be prepared for number 0 - 9?
'''



# PREPARE DATA BEGIN ===============================

number_count_dict = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0
}

# MAIN PROGRAM BEGIN ===============================

for door_number in range(1, 2001):

    pass # place holder, I expect you to replace my place holder with your actual code

    '''
    Now you have a int value - door_number, for example: 1345 / 3
    
    Question:
    How to convert 1345 to int 1 / 3 / 4 / 5, then you can accumulate them to your dict
    How to convert 3 to int 0 / 0 / 0 / 3, then you can accumulate them to your dict
    
    '''



print(number_count_dict)

