'''
Requirement:
Find the 2 maximum and 2 minimum values of the tup1, and create a new tuple from the 4 values.
'''

# tup1 = (10, 30, 50, 20, 60, 40)
tup1 = (10, 30, 50, 20, 60, 40, 100, -1000, 95, 46, 87)




def test1():

    sorted_list = sorted(tup1)

    for item in enumerate(sorted_list):
        print(f"{item}. Its type is {type(item)}")
        index, value = item # tuple unpacking
        print(index, value)
        print("-" * 50)


'''
IMPORTANCE!!! ------------------------------------
1) sorted() helps create a new sorted list from your tuple / list
2) enumerate(list) combines index and value into a tuple
   enumerate(list) returns a list of tuples
3) Global Search shortcut key: Ctrl + Shift + F, help revise our knowledge
-------------------------------------------------
'''

# solution 1: sorted + enumerate loop ------------------------

def solution1():

    result_list = []


    sorted_list = sorted(tup1)

    for index, value in enumerate(sorted_list):

        # the value range of index is [0, len(sorted_list)-1]

        if index < 2 or index > len(sorted_list) - 3:
            result_list.append(value)


    result_tuple = tuple(result_list)
    print(result_tuple)


# solution 2: slice ------------------------------------


def solution2():
    sorted_list = sorted(tup1)
    result_tuple = tuple(sorted_list[:2] + sorted_list[-2:])
    print(result_tuple)



# test1()

solution1()