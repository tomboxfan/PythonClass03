# revise 0073

set_divisible_by_2 = set(range(0, 20, 2))
set_divisible_by_3 = set(range(0, 20, 3))
set_divisible_by_5 = set(range(0, 20, 5))







print(set_divisible_by_2)
print(set_divisible_by_3)
print(set_divisible_by_5)

print("Union - 并集 ----------------------------")
set_divisible_by_2_or_5 = set_divisible_by_2.union(set_divisible_by_5) # set class union function/method
print("set_divisible_by_2_or_5: ", set_divisible_by_2_or_5)

set_divisible_by_2_or_5 = set_divisible_by_2 | set_divisible_by_5 # pipe operator
print("set_divisible_by_2_or_5: ", set_divisible_by_2_or_5)


print("Intersection - 交集 ----------------------------")
set_divisible_by_2_and_5 = set_divisible_by_2.intersection(set_divisible_by_5) # set class intersection function/method
print("set_divisible_by_2_and_5: ", set_divisible_by_2_and_5)

set_divisible_by_2_and_5 = set_divisible_by_2 & set_divisible_by_5 # and operator
print("set_divisible_by_2_and_5: ", set_divisible_by_2_and_5)


print("Difference/Minus - 差集 ----------------------------")
set_divisible_by_2_but_not_5 = set_divisible_by_2.difference(set_divisible_by_5) # set class difference function/method
print("set_divisible_by_2_but_not_5: ", set_divisible_by_2_but_not_5)

set_divisible_by_2_but_not_5 = set_divisible_by_2 - set_divisible_by_5 # minus operator
print("set_divisible_by_2_but_not_5: ", set_divisible_by_2_but_not_5)


print("Symmetric Difference - 对称差集 ----------------------------")
set_divisible_by_2_or_5_but_not_both = set_divisible_by_2.symmetric_difference(set_divisible_by_5) # set class symmetric_difference function/method
print("set_divisible_by_2_or_5_but_not_both: ", set_divisible_by_2_or_5_but_not_both)

set_divisible_by_2_or_5_but_not_both = set_divisible_by_2 ^ set_divisible_by_5
print("set_divisible_by_2_or_5_but_not_both: ", set_divisible_by_2_or_5_but_not_both)



print("Union = Intersection + Symmetric Difference / 并集 = 交集 + 对称差集 ----------------------------")
print("Union = Intersection + Symmetric Difference : ", set_divisible_by_2_or_5 == (set_divisible_by_2_and_5 | set_divisible_by_2_or_5_but_not_both))