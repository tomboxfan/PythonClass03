def unpacking_example1():
    student_info = ('John', 'T011233E', 'Oct 10th, 2007', 'Male')

    '''
    it looks like: ungroup tuple student_info, assign its value to multiple variable.
    Actually,
    On the left side, it is a tuple which contains 4 variables - name, ic, birthday, gender 
    So, this is assigning a tuple's value on the right to a tuple variable on the left
    '''
    name, ic, birthday, gender = student_info
    print(name, ic, birthday, gender)

    (name, ic, birthday, gender) = student_info
    print(name, ic, birthday, gender)



def unpacking_example2():
    x = 'jelly'
    y = 'bean'
    print(x, y)


    '''
    create a tuple on the right
    create another tuple on the left
    assign tuple on the right to the tuple on the left
    '''
    x, y = y, x
    print(x, y)

    (x, y) = (y, x)
    print(x, y)


def unpacking_example3():
    (a, (b, (c, d))) = (4, (3, (2, 1)))
    print(a, b, c, d)

    a, (b, (c, d)) = (4, (3, (2, 1)))
    print(a, b, c, d)





unpacking_example3()