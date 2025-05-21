# Program to find the word count in sentence.

#Original sentence
sentence = "apple banana apple grape banana apple"

#Declaring Empty dictionary
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
 
print(word_count)
