'''
Logic:

There are several boundaries in the question.
1) 10% of the 1st million profit
2) 7.5% of the 2nd million profit
3) 5% of the 3rd and 4th million profit
4) 3% of the 5th and 6th million profit
5) 1.5% of the 7th, 8th, 9th, 10th million profit
6) 1% of the remaining profit

         ====================
         threshold
         ====================
         above    1%
         --------------------
         4m      1.5%
         --------------------
         2m      3%
         --------------------
         2m      5%
         --------------------
   ^      1m      7.5%
   |      --------------------
   |      1m      10%
 -----------------------------------------------
'''



# Step 1) Define variable profit
profit = int(input("Total profit for the year:"))

# Step 2) I use float constructor to create a float variable which equals to 0
bonus = float()

# Step 3) Define variable thresholds and rates which represent the table definition above
thresholds = [1000000, 1000000, 2000000, 2000000, 4000000] # 5 numbers
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01] # 6 numbers


'''

I need to check whether the profit exceeds the thresholds value.

---------------------------------------------------------------------------
    MY LOGIC                             MY CODE
---------------------------------------------------------------------------
[tier 1]

if profit <= 1,000,000                  if profit < threshold[0]:
    bonus = profit * 0.1                    bonus += profit * rates[0]
    finish                                  finish

if profit > 1,000,000                   if profit > threshold[0]:
    bonus = 1,000,000 * 0.1                 bonus += threshold[0] * rates[0]
    profit -= 1,000,000                     profit -= threshold[0]
    go to [tier 2]                          go to [tier 2]



[tier 2]

if profit <= 1,000,000                  if profit < threshold[1]:
    bonus = bonus + profit * 0.075          bonus += profit * rates[1]
    finish                                  finish

if profit > 1,000,000                   if profit > threshold[1]:
    bonus += 1,000,000 * 0.075               bonus += threshold[1] * rates[1]
    profit -= 1,000,000                     profit -= threshold[1]
    go to [tier 3]                          go to [tier 3]



[tier 3]

if profit <= 2,000,000                  if profit < threshold[2]:
    bonus = bonus + profit * 0.05           bonus += profit * rates[2]
    finish                                  finish

if profit > 2,000,000                   if profit > threshold[2]:
    bonus += 2,000,000 * 0.05               bonus += threshold[2] * rates[2]
    profit -= 2,000,000                     profit -= threshold[2]
    go to [tier 4]                          go to [tier 4]


[tier 4]
... ....


[tier 5]
... ....

[tier 6]

    bonus += profit * 0.01            bonus += profit * rate[5]
'''


# the for loop covers tier 1 to tier 5
for i in range(len(thresholds)):    # range(len(thresholds)) -> range(5) -> 0 to 4 -> [tier 1] - [tier 5]

    if profit <= thresholds[i]:
        bonus += profit * rates[i]
        print(f"We should keep {bonus} to our staff for this outlet.")
        exit()

    bonus += thresholds[i] * rates[i]
    profit -= thresholds[i]

# [tier 6]
bonus += profit * rates[5]
print(f"We should keep {bonus} to our staff for this outlet.")

