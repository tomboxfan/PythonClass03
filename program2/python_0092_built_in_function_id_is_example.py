


# id(): tell you the address of some variable -----------------------

c = 5
print(id(c))

d = True
print(id(d))

e = 'Hello'
print(id(e))



a = [1,2,3]
print(id(a))

b = [4,5,6]
print(id(b))


print("---------------------------------")
# is example --------------------------------------

b = a

print("a == b : ", a == b ) # True
print('Address of a: ', id(a))
print('Address of b: ', id(b))
print("id(a) == id(b) : ", id(a) == id(b))

print('a is b: ', a is b) # True

print("---------------------------------")

c = [1,2,3]
print("a == c: ", a == c) # True
print('id(a) == id(c): ', id(a) == id(c)) # False
print("a is c: ", a is c) # False

print("---------------------------------")
x = 10
print(id(x))
x += 2
print(id(x))
