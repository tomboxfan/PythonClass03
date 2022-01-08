# Requirement: calculate the sum from 1 to 100

# Solution 1 - use simple for range loop
sum_value1 = 0

for i in range(1, 101):
    sum_value1 += i

print(f'Sum from 1 to 100 is {sum_value1}')


# Solution 2 - use built-in function sum
# sum() calculate the total value of all the numbers
sum_value1 = sum(range(1, 101))
print(f'Sum from 1 to 100 is {sum_value1}')