sentence = "  I love learning Python  "

print(sentence)
print(sentence.strip())
print(sentence.replace("Python", "programming"))

words = sentence.strip().split()
for word in words:
    print(word)