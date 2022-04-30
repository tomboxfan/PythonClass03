# When unpacking, you may sometimes want to discard certain values.
# You use underscore to represent, you don't need this variable
buy_order = ('DBS', 100, 29.97, '2022, 4, 30')
_, shares, price, _ = buy_order

total_cost = shares * price
print(f"For this buy order, you need to pay ${total_cost}")


# Another example
# In my loop body, I don't need this looping variable. I can just use underscore the represent: I don't want it / need it
for _ in range(10):
    print("Hello Python!")
