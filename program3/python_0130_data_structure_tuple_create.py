'''

--------------------
tuple
--------------------

tuple is highly-similar to list.

Differences between tuple and list:

1) list is mutable, tuple is immutable.
   Once a tuple is created, you cannot change it.

2) You use [] in list, you use () in tuple

'''


def create_tuple_example():

    print("empty tuple and empty list -----------------------")
    tup_empty = ()
    list_empty = []
    print(tup_empty)
    print(list_empty)

    print("single value tuple and list ----------------------")
    tup_1 = (50,) # comma is mandatory as (50) is same as 50
    list_1 = [50]
    print(tup_1)
    print(list_1)

    print("multiple values tuple and list ----------------------")
    tup_multiple = (1, 2, 3, 4, 5)
    list_multiple = [1, 2, 3, 4, 5]
    print(tup_multiple)
    print(list_multiple)

    list_multiple[0] = -1
    print(list_multiple)

    # tup_multiple[0] = -1 # error! because, tuple is immutable








create_tuple_example()