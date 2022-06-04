
def example1():

    list1 = list(range(10))
    tup1 = tuple(range(10))
    range1 = range(10)
    str1 = "The rocket came back from Mars"

    l1 = [n * 2           for n in list1            if n % 2 == 1 ]
    print(l1)


    l2 = [n * 3           for n in tup1             if n < 5 ]
    print(l2)

    l3 = [n + 1           for n in range1           if 3 < n < 8 ]
    print(l3)

    l4 = [ch.upper()      for ch in str1            if ch in 'aeiou' ]
    print(l4)

# example1()


'''
Requirement:
Use list comprehension to define a int list which contains 10 0
'''
def example2():
    l1 = [0] * 10
    print(l1)

    l2 = [0     for _ in range(10)]
    print(l2)

example2()

