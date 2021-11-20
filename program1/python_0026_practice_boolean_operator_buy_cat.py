# Requirement: A customer walks into a Pet's store, he said, 'I want a
# male cat, white or yellow
# Or a female cat, not white
# Or just a black cat
# You need to get input from console about cat gender and cat color
# You program needs to tell whether the customer wants it or not


gender = input("Is the cat male or female? ")
color = input("What's the color of the cat? ")

'''
The cat which the customer wants falls into 3 categories:
1) gender == 'male' and (color == 'white' or color == 'yellow')
2) gender == 'female' and color != 'white'
3) color == 'black'

We join 'or' the join the 3 cateogries together.
'''

if gender == 'male' and (color == 'white' or color == 'yellow')   or   gender == 'female' and color != 'white'   or    color == 'black':
    print("I will take it")
else:
    print("I don't want it")