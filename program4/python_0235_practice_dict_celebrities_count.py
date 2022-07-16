'''
There is a party to celebrate celebrities that you get to attend because you
won a ticket at your office lottery. Because of the high demand for tickets,
you only get to stay for one hour, but you get to pick which hour because
you received a special ticket. You have a schedule that lists exactly when
each celebrity is going to attend the party. You want to get as many pictures
with celebrities as possible to improve your social standing. This means you
wish to go for the hour when you get to hobnob with the maximum number
of celebrities and get selfies with each of them.

We are given a list of intervals that correspond to when each celebrity
comes and goes. Assume that these intervals are [i, j), where i and j
correspond to hours. That is, the interval is closed on the left side and open
on the right side. This means the celebrity will be partying on and through
the ith hour, but will have left when the jth hour begins. So even if you
arrive on the dot on the jth hour, you will miss this particular celebrity.
Here’s an example:

Celebrity   Comes   Goes
Beyoncé     6       7
Taylor      7       9
Brad        10      11
Katy        10      12
Tom         8       10
Drake       9       11
Alicia      6       8
'''


# PREPARE DATA BEGIN -----------------------------------

# Step 1) Prepare list
# celebrities_arrival_schedule = [(6, 7), (7, 9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8)]

celebrities_arrival_schedule = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]



















































# Step 2) Prepare dict
# I define a dict, which remembers how many celebrities will come for the hour
# key       : hour
# value     : celebrities count
celebrities_count = {6:0, 7:0, 8:0, 9:0, 10:0, 11:0}


# MAIN PROGRAM BEGIN -----------------------------------

# Step 3) fill up dict
# Loop celebrities_arrival_schedule, process each person, update my dict
for time_interval in celebrities_arrival_schedule:

    for hour in range(*time_interval):
        celebrities_count[hour] += 1

print("LOG - here is my dict, which shows how many celebrities will come for each hour:")
print("LOG - hour: celebrities count")
print(celebrities_count)

# Step 4) Max the answer, loop the dict

hour_i_should_go = 6
celebrities_i_can_see = 0

for key, value in celebrities_count.items():

    if value > celebrities_i_can_see:
        hour_i_should_go = key
        celebrities_i_can_see = value


# Step 5） print the answer
print(f"I should go to the party at {hour_i_should_go}pm")



#

