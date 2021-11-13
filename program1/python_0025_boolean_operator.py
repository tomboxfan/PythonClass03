
print("And rule -------------------------")
print(f"True and True is {True and True}")
print(f"True and False is {True and False}")
print(f"False and True is {False and True}")
print(f"False and False is {False and False}")


print("Or rule -------------------------")
print(f"True or True is {True or True}")
print(f"True or False is {True or False}")
print(f"False or True is {False or True}")
print(f"False or False is {False or False}")

print("Not rule -------------------------")
print(f"not True is {not True}")
print(f"not False is {not False}")


bool_a = True
bool_b = False
bool_c = True
bool_d = False

# and - any value is False, the whole value is False
print(bool_a and bool_b and bool_c and bool_d) # False

# or - any value is True, the whole value is True
print(bool_a or bool_b or bool_c or bool_d) # True


# or - lowest priority, so it equals to
# bool_a and bool_b             or              bool_c and bool_d
print(bool_a and bool_b or bool_c and bool_d) # False


# it equals to
# bool_a     and    (bool_b or bool_c)     and        bool_d
print(bool_a and (bool_b or bool_c) and bool_d) # False


# Not - highest priority, so it equals to
# bool_a     and      not boo_b       and       bool_c        and       not bool_d
print(bool_a and not bool_b and bool_c and not bool_d)  # True

