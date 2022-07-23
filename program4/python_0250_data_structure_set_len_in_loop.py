def len_example():
    int_set = {1, 2, 3}
    print(f"int_set size is: {len(int_set)}")

def in_example():
    int_set = {1, 2, 3}
    print(f"Is 4 in the set? {4 in int_set}")
    print(f"Is 1 in the set? {1 in int_set}")

def loop_example():
    int_set = {1, 2, 3}
    for x in int_set:
        print(x)

len_example()
in_example()
loop_example()