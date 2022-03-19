'''
There are 5 girls and 5 boys.

They are defined as 2 list as below:
girls = ['Olivia','Emily','Lily','Emma','Mary']
boys = ['Jack','David','Robert','James','John']

Your program need to randomly(0039) divide them into 5 groups. Each group contains 1 boy & 1 girl.

'''

import random

# PREPARE DATA BEGIN -----------------------------

girls = ['Olivia','Emily','Lily','Emma','Mary']
boys = ['Jack','David','Robert','James','John']

# MAIN PROGRAM BEGIN -----------------------------

# Logic: I can loop 4 times, each time randomly select a boy, randomly select a girl, team up, remove them for the 2 lists.

for i in range(4):

    boy_index = random.randint(0, len(boys) - 1)
    girl_index = random.randint(0, len(girls) - 1)

    print(girls[girl_index], boys[boy_index])

    girls.pop(girl_index)
    boys.pop(boy_index)

print(girls[0], boys[0])
# shortcut key: ctrl + / -> comment / uncomment a line