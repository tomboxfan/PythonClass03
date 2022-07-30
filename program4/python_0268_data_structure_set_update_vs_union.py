

def update_example():

    a_set = {1, 2, 3}
    print(a_set)

    a_set.update([2, 3, 4]) # add a list to the set
    print(a_set) # {1, 2, 3, 4}

    a_set.update({3, 4, 5}) # add a set to the set
    print(a_set) # {1, 2, 3, 4, 5}

    a_set.update((4, 5, 6)) # add a tuple to the set
    print(a_set) # {1, 2, 3, 4, 5, 6}

def union_example():

    a_set = {1, 2, 3}
    print(a_set)

    a_set = a_set.union([2, 3, 4]) # add a list to the set
    print(a_set) # {1, 2, 3, 4}

    a_set = a_set.union({3, 4, 5}) # add a set to the set
    print(a_set) # {1, 2, 3, 4, 5}

    a_set = a_set.union((4, 5, 6)) # add a tuple to the set
    print(a_set) # {1, 2, 3, 4, 5, 6}


# update_example()

union_example()


'''
1) update() is quite similar to union()
   update() will update the original set.
   union() will leave the original set alone.
'''
