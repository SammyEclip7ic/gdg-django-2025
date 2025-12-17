sentence = input("Enter a sentence to see it neatly displayed in a dictionary: ")

words_frequency = {}

list_of_words = sentence.split()
for word in list_of_words:
    if word in words_frequency:
        freqency = words_frequency[word]
        words_frequency[word] = freqency + 1
    else:
        words_frequency[word] = 1

print(words_frequency)
