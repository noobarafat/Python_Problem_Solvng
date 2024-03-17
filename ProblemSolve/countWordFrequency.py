# count word frequency

sentence = ("Hello, this this This is K. M. Arafat Islam. I am Studying at Daffodil Int. University in the department "
            "ofSE")
sentence = sentence.lower()
words = sentence.split()

dict = {}

for word in words:
    dict[word] = 0
for word in words:
    count = words.count(word)
    dict[word] = count

print(dict)