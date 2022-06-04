def cooking(dish1, dish2):
    print(f"Start cooking: {dish1}")
    print(f"Start cooking: {dish2}")

# cooking("fish", "pork")

def playing(game):
    print(f"Start playing: {game}")

# playing("Counter Strike")

def coding(language, type, deadline):
    print(f"Start coding {language} {type}, it should be finished by {deadline}")

# coding("Python", "Homework", "Wednesday")


# Our main program begins ---------------------
actions = [
    ('COOKING', 'fish', 'pork'),
    ('PLAYING', 'badminton'),
    ('CODING', 'C++', 'Project', 'End of month')
]

for   action, *arguments      in actions: # learnt in 154, star unpacking

    if action == 'COOKING':
        cooking(*arguments)  # learnt in 117, star unpacking

    elif action == 'PLAYING':
        playing(*arguments)

    elif action == 'CODING':
        coding(*arguments)


'''
Please revise 117 / 118 / 154
'''

