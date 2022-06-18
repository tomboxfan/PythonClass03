'''
Requirement:
I have a very long sentence as below:
"I hope that a study of very long sentences will arm you with strategies that are almost as diverse as the sentences themselves, such as: starting each clause with the same word, tilting with dependent clauses toward a revelation at the end, padding with parentheticals, showing great latitude toward standard punctuation, rabbit-trailing away from the initial subject, encapsulating an entire life, and lastly, as this sentence is, celebrating the list."

I want to know
1) how many distinct words it has in total.
2) how many times each word appears in the sentence.
'''

# Step 1) I define the sentence as a string value
sentence = "I hope that a study of very long sentences will arm you with strategies that are almost as diverse as the sentences themselves, such as: starting each clause with the same word, tilting with dependent clauses toward a revelation at the end, padding with parentheticals, showing great latitude toward standard punctuation, rabbit-trailing away from the initial subject, encapsulating an entire life, and lastly, as this sentence is, celebrating the list."

# Step 2) I use split() function to split the sentence into word list
word_list = sentence.split()

# Step 3) print log msg to the confirm, word_list contains the correct data
print(f'LOG - the word list is: {word_list}')

# Step 4) define a dict variable word_dict, to summarize how many times each word appears.
# key: the word
# value: how many times it appears.
word_dict = {}


# there is no duplicate key in a dict!

# Step 5) handle those words one by one
for word in word_list:

    # remove special characters
    word = word.replace(",", "")
    word = word.replace(".", "")
    word = word.replace(":", "")

    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] = word_dict[word] + 1

    '''
    if the variable appears on the right side of '=', means, you are using its value
    if the variable appears on the left side of '=', means, you are assigning a new value to the variable
    '''

    print(f"LOG - Now key '{word}' in word_dict has value: {word_dict[word]}")
    print(f"LOG - word_dict is: {word_dict}")
    print(f"LOG ---------------------------------------------------------------------------")

    '''
    LOG msg helps you to make sure your code is good so far, when you finish your program, all log msgs can be deleted!
    '''

# Step 6) Let's print out the result
print(f"There are in total {len(word_dict)} distinct words")

# Step 7) Loop the dict to print out how many times each word appears.
for key, value in word_dict.items():
    print(f"{key}: {value} times")


'''
IMPORTANCE!!! ---------------------------------------
1) function split() helps convert str to a list

2) Periodically, print out log msg to make sure variables have correct value

3) function .items() helps loop a dictionary

4) function replace('a', 'b') helps replace all letters 'a' to 'b' in your original str

5) comment out all LOG msg as the last step
-----------------------------------------------------
'''