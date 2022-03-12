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

# Logic: Loop all the girls. Randomly select a boy to team up with the girl


# Version 1

# for girl in girls:
#     boy_index = random.randint(0, 4)
#     boy = boys[boy_index]
#     print(girl, boy)




# Version 2

for girl in girls:
    boy_index = random.randint(0, len(boys)-1)
    boy = boys[boy_index]
    print(girl, boy)
    boys.pop(boy_index)

