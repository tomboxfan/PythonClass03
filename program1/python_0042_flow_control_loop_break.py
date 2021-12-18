

a = 0
print("While loop starts: ")


'''
IMPORTANT!!! -------------------------------------------------
'break' will terminate the loop, very useful in a dead loop
'break' will make your loop stop immediately and move on to the next line of code
while True / break comination is very common.
--------------------------------------------------------------
'''
while True:
    a += 1
    if a == 3:
        break
    print(a)

print("while loop ends.")

# HOMEWORK
# refactor 0041, counting sheep. when counting sheep to 50, break out of the while loop.

sheep_count = 0
while True:
    print(f"{sheep_count} sheep, I feel sleepy...")
    sheep_count += 1

    if sheep_count > 50:
        break

