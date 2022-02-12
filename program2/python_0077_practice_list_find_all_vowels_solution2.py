
'''
Requirement:
User will supply a word from console.
Requirement 1) You need to find all the vowels(a/e/i/o/u) in the word.
Requirement 2) Further enhance your code, only collect vowels once (we don't want duplicate vowels)

Answer solution 2 is far below...
'''































# PREPARE DATA BEGIN ---------------------------------

# I need to store 5 vowels letter into a list, so that I can check whether some letter is a member of the list or not
vowels = list("aeiou")

# I need a variable which is to store the word given by user
word = input("Please give me the word:")

# I need a container which is to hold all found vowels in word
found = []


# MAIN PROGRAM BEGIN ---------------------------------

for letter in word:

    if letter in vowels:
        found.append(letter)

        # Remove the vowel from vowels list

        # Solution 1
        # vowels.remove(letter)

        # Solution 2
        letter_index = vowels.index(letter)
        vowels.pop(letter_index)

for vowel in found:
    print(vowel, end=' ')


