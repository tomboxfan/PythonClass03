

# By default, print() inserts a space between the items it prints.
print(1,2,3)

# But you can specify a 'separator' argument to tell python, how to separate those items.
print(1,2,3, sep='-') # separator
print(1,2,3, sep=' * ')
print(1,2,3, sep='\n') # next line character

print('----------------------------------------')


#By default, print() adds a extra \n at the end of what it prints.
for i in range(5):
    print(i) # You never specify end argument value, so python will use '\n' as 'end' argument value.

#You can customize the end of line character as well.

print('----------------------------------------')
for i in range(5):
    print(i, end=' ')