def add_example():
    k = {81, 180}
    print(k)

    k.add(54)
    print(k)

    k.add(12)
    print(k) # set is unordered.

    k.add(180)
    print(k) # set doesn't allow duplicate values


def remove_example():
    k = {81, 180}
    print(k)

    k.remove(81)
    print(k)

    if 82 in k:
        k.remove(82) # KeyError: 82
        print(k)


def discard_example():
    k = {81, 180}
    print(k)

    k.discard(81)
    print(k)

    k.discard(82)
    print(k)    # no error happens, it just does nothing.





# add_example()
# remove_example()
discard_example()

'''
IMPORTANCE!!! --------------------------------
1) a_set.remove(value)  can cause KeyError
2) a_set.discard(value)  WON'T cause KeyError
-----------------------------------------------
'''