txt1 = 'welcome to the jungle'
word_list1 = txt1.split()
print(word_list1) # ['welcome', 'to', 'the', 'jungle']


txt2 = 'Hello, my name is Peter, I am 26 years old'
word_list2 = txt2.split(", ") # every time you see this separator, please help cut my original str
print(word_list2) # ['Hello', 'my name is Peter', 'I am 26 years old']

word_list3 = txt2.split(',')
print(word_list3) # ['Hello', ' my name is Peter', ' I am 26 years old']

txt3 = 'apple#banana#cherry#orange'
fruits_list = txt3.split("#")
print(fruits_list) # ['apple', 'banana', 'cherry', 'orange']