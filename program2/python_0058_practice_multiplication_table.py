'''
Requirement:
Output the multiplication table as below
'''

'''
Logic is always the most important! When logic is clear, then we can convert the logic to code.

Logic:
1) I can see there are in total 9 lines -> I loop for i in range(1, 10):

2) In each line, there are very similar items.
   In 1st row, there is 1 item
   In 2nd row, there are 2 items
   In 3rd row, there are 3 items
   ....
   In 9th row, there are 9 items
   ->
   for each row, I loop in range (1, i+1):
   
3) All those items are in same line -> I should use parameter end=' ' in the print statement.
   
'''

for row in range(1, 10):
    for item_index in range(1, row + 1):
        print(f"{item_index} * {row} = {row * item_index}", end = ' ')
    print('')

'''
----------------
More explanation:
----------------

Line 25:
It will loop 9 times, during these 9 times, row = 1 / 2 / 3 / 4 .... / 9

Line 26:
When row = 1, Code 26 becomes    for item_index in range(1, 2):    this will loop 1 times.
When row = 2, Code 26 becomes    for item_index in range(1, 3):    this will loop 2 times.
....
When row = 9, Code 26 becomes    for item_index in range(1, 10):   this will loop 9 times.


'''