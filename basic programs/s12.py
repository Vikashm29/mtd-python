sentence = "The fox jumps over the lazy dog"

#get wordd that longer than 3
long_words = [word for word in sentence.split() if len(word) > 3]

print(long_words)