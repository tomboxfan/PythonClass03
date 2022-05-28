'''
list comprehension: Create a list from an existing list / tuple / range / str
'''

def list_comprehension():

    print("Example 1: create a new list from an existing list -------------------------------")

    l1 = [9, 5, 2]
    # Requirement: create a new list l2 which contains [8, 4, 1]

    l2 = []
    for n in l1:
        l2.append(n - 1)
    print(l2)


    l2 = [n - 1   for n in l1] # equals to line 12 - 14
    print(l2)


    print("Example 2: create a new list from an existing tuple -------------------------------")

    t1 = 1, 5, 7
    # Requirement: create a new list l3 which contains [3, 15, 21]
    l3 = [n * 3 for n in t1]
    print(l3)


    print("Example 3: create a new list from an existing range -------------------------------")

    r1 = range(5)
    # Requirement: create a new list l4 which contains [0, 2, 4, 6, 8]
    l4 = [n * 2 for n in r1]
    print(l4)

    print("Example 4: create a new list from an existing str -------------------------------")

    str = 'hello'
    # Requirement: create a new list l5 which contains ['H', 'E', 'L', 'L', 'O']
    l5 = [ch.upper() for ch in str]
    print(l5)





list_comprehension()

'''
IMPORTANCE!! -----------------------------
List comprehension:
inside the square bracket: 
in the front: loop body
in the back: loop expression
[n - 1     for n in l1]

The loop expression will be added as a new value to list  
------------------------------------------
'''