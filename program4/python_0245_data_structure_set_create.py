def using_curly_braces():
    set1 = {1, 2, 3, 4, 5}
    print(f"set1 = {set1}")
    print(f"set1 is of type {type(set1)}")
    print("----------------------------------------")

    dict = {}
    print('{} is a ', type(dict))


def using_set_constructor_from_list_tuple_range_str():

    set2 = set()
    print("set2 = ", set2)
    print("------------------------------")


    # create a set using a list
    a_list = [1, 1, 2, 2, 3, 3]
    set3 = set(a_list)
    print("set3 = ", set3)
    print("------------------------------")

    set4 = set([1, 1, 2, 2])
    print("set4 = ", set4)
    # the square brackets inside belong to the list
    # the parentheses outside belong to the set constructor
    print("------------------------------")

    #create a set using a tuple
    set5 = set((1, 1, 2, 2))
    print("set5 = ", set5)
    # the parentheses inside belong to the tuple
    # the parentheses outside belong to the set constructor
    print("------------------------------")

    # create a set using a range object
    range1 = range(1, 10)
    set6 = set(range1)
    print("set6 = ", set6)
    print("------------------------------")

    # create a set using a str
    set7 = set("Hello Python!")
    print("set7 = ", set7)
    print("------------------------------")




def using_set_constructor_from_dict():
    dict1 = {1:'a', 2:'b', 3:'c'}

    # remember: when we loop a dict, we are actually looping its key
    # so when we create a new set from a dictionary, we are actually creating a new set from the dictionary's key as well.
    set8 = set(dict1)
    print("set(dict1) gives you a set with dict1's keys")
    print("set8 = ", set8)
    print("------------------------------")

    set9 = set(dict1.values())
    print("set(dict1.values()) gives you a set with dict1's values.")
    print("set9 = ", set9)
    print("------------------------------")

    set10 = set(dict1.items())
    print("set(dict1.items()) gives you a set with dict1's key/value pairs.")
    print("set10 = ", set10)
    print("------------------------------")









# using_curly_braces()
# using_set_constructor_from_list_tuple_range_str()
using_set_constructor_from_dict()


'''
IMPORTANCE!!! --------------------------------------
1) set is unordered
2) duplicate values are only kept ONCE


3) about 'iterable'
You can put an 'iterable' object into the set constructor -> set()
What is an 'iterable' object? 
list is iterable         because     for v in a_list:
tuple is iterable        because     for v in a_tuple:
range is iterable        because     for i in range(10):
str is iterable          because     for ch in "Python":
dict is iterable         because     for key in dict:
                                     for key in dict.keys():
                                     for value in dict.values():
                                     for key, value in dict.items():
                                     
What is an 'iterable' object?
1) an iterable object is capable of returning its members one by one.
1) an iterable object is anything that you can loop over with a for loop.
'''