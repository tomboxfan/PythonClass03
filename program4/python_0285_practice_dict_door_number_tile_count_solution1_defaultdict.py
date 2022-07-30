'''
There is big resort, it has 2000 rooms.
Door number tiles need to be installed for all these 2000 rooms, starting from '0001' to '2000'.
Door number is composed of 4 tiles. i.e.
'0001' is composed of 3 '0' and 1 '1';
'2000' is composed of 3 '0' and 1 '2'.

Question:
How many tiles need to be prepared for number 0 - 9?
'''


'''
Requirement:
change this program to use defaultdict
'''






# PREPARE DATA BEGIN ===============================

number_count_dict = {
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0
}

# MAIN PROGRAM BEGIN ===============================

for door_number in range(1, 2001):

    # Step 1) calculate tile '0' count in front of door_number when its digit count is not 4
    if door_number < 10:
        number_count_dict['0'] += 3
    elif door_number < 100:
        number_count_dict['0'] += 2
    elif door_number < 1000:
        number_count_dict['0'] += 1

    # Step 2) check how many tiles the actual door_number needs.
    for tile in str(door_number):
        number_count_dict[tile] += 1


print(number_count_dict)

