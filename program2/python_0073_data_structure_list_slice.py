'''
IMPORTANTCE!!! --------------------------------------------
Assume L is a list
expression L[start:stop:step] returns a portion of list L
The portion starts from index start(inclusive) to index stop(exclusive), at a step size step.

Syntax: L[start:stop:step]
start: start position
stop:  stop position
step:  the increment
-----------------------------------------------------------
'''

L = list('abcdefghi')
print(L)


'''
positive index :      0    1    2    3    4    5    6    7    8
                    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
negative index :     -9   -8   -7   -6   -5   -4   -3   -2   -1

'''

print("1) Basic Example -------------------------------")

print(L[2:7])
# L[2:7] doesn't have step, so Python assume step equals to 1
# L[2:7] equals to L[2:7:1]
print(L[2:7:1])

print("2) Slice with Negative Indices ------------------------")
print(L[-7:-2])
print(L[-7:-2:1])

print("3) Slice with Positive & Negative Indices ------------------------")
print(L[2:-5])

print("4) Specify Step of the slicing ------------------------")
print(L[2:7:2])

print("5) Negative Step Size ------------------------")
print(L[6:1:-2])

print("6) Slice at Beginning & End ------------------------")
print(L[:3])
# L[:3] equals to L[0:3]

print(L[6:])
# L[6:] equals to L[6:len(L)]

print("7) Reverse a list ------------------------")
print(L[::-1])
# Because it doesn't start & stop, so the slice starts from beginning till end.


print("8) Modify multiple list values ------------------------")
L = list("abcde")

'''
positive index:   0    1    2    3    4
                ['a', 'b', 'c', 'd', 'e']
negative index:  -5   -4   -3   -2   -1 
'''

L[1:4] = [1,2,3]
print(L)

L = list("abcde")
L[1:2] = [1,2,3]
print(L)

print("9) Insert multiple list items ------------------------")
L = list('abc')

'''
positive index:   0    1    2  
                ['a', 'b', 'c']
negative index:  -3   -2   -1 
'''

L[:0] = [1,2,3]
# start is missing, Python assumes slice starts from the left beginning.
# L[:0] equals to L[0:0]
# When start equals to stop, it points to a position
# So, when you assign a list to a position of L, you actually insert list [1,2,3] into list L at position 0.


print(L)

L = list('abc')
L[len(L):] = [1,2,3]
# stop is missing, Python assumes slice stop till the end.
# L[len(L):] equals to L[len(L):len(L)]
# When start equals to stop, it points to a position
# So, when you assign a list to a position of L, you actually insert list [1,2,3] into list L at position 0.
print(L)

