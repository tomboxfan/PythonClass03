dict_1 = {
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0
}

# Step 1) Import defaultdict from collections module
from collections import defaultdict

# Step 2) Create defaultdict object using defaultdict constructor, and pass in 'int' constructor to it.
# Meaning, if the key doesn't exist in the defaultdict, defaultdict will call the 'int' constructor to create a value, and insert the value for the key into the defaultdict.
defaultdict_int = defaultdict(int) # 'int' means int(). int() will create int value 0

print(f"defaultdict_int size is: {len(defaultdict_int)}")

for ch in '0123456789':
    print(f"key: {ch} is found in defaultdict_int with value: {defaultdict_int[ch]}")

print(f"defaultdict_int size is: {len(defaultdict_int)}")

print(defaultdict_int)