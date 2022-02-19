'''
Requirement:
You have 2 SORTED lists, merge the 2 lists into 1 new list. And this new list is SORTED as well.

merge
list_a = [1,5,7,9,13,15,24,27,78,110,167]
list_b = [2,2,6,8,16,17,18,19,99]
to new_list
'''


'''
Logic / Algorithm:
Step 1) I create 2 pointers index_a and index_b, their initial value are 0, so that they point to the 1st value of list_a and list_b
Step 2) I loop forever as the exit condition is very complex, meaning I can only use 'while True / break' loop
Step 3) Inside the loop body, I compare the 2 values which index_a and index_b points to.
        I append the smaller value to the result list, and move the index_a or index_b to the next position.
        There are 3 situations:
        
        Situation 1) list_a has reached the end, list_b has NOT reached the end.
        -> append the remaining values of list_b to new_list
           then break the loop -> program finishes!
        
        Situation 2) list_a has NOT reached the end, list_b has reached the end.
        -> append the remaining values of list_a to new_list
           then break the loop -> program finishes!
        
        Situation 3) list_a has NOT reached the end, list_b has NOT reached the end.
        -> I compare list_a[index_a] vs list_b[index_b]. I append the smaller value to new_list and move the index to the next. Loop continue.

Notes. 
1) Situation 1 and 2 are 'edge cases'.
2) Situation 3 is 'happy flow'.
3) Q) How to tell whether a list has reached the end? 
   A) index_a == len(list_a) 
   
   if len(list_a) is 10, then list_a index value is from 0 - 9.
   So, when index_a == len(list_a), then index_a becomes invalid, means index_a is at the end of list_a. 
'''

# PREAPRE DATA BEGIN =============================

list_a = [1,5,7,9,13,15,24,27,78,110,167]
list_b = [2,2,6,8,16,17,18,19,99]

# list_a = [1,5,7]
# list_b = [2,2,6,8,16,17,18,19,99]

# list_a = []
# list_b = [2,2,6,8,16,17,18,19,99]


# this is to hold the final result
new_list = []

# these 2 pointers point to the 1st value of list_a and list_b
index_a = 0
index_b = 0

# MAIN PROGRAM BEGIN =============================
while True:

    # Situation 1) list_a has reached the end
    if index_a == len(list_a):
        new_list.extend(list_b[index_b:]) # append the remaining value of list_b to new_list
        break

    # Situation 2) list_b has reached the end.
    if index_b == len(list_b):
        new_list.extend(list_a[index_a:])
        break

    # Situation 3) list_a has NOT reached the end, list_b has NOT reached the end.
    if list_a[index_a] < list_b[index_b]:
        new_list.append(list_a[index_a])
        index_a += 1
    else:
        new_list.append(list_b[index_b])
        index_b += 1

print(new_list)


'''

Further Observation:

Because: each time, we move either list_a's pointer or list_b's pointer to the next
So: list_a and list_b won't reach the end at the same time.

So:
We can simplify situation 1) and situation 2) 
'''
