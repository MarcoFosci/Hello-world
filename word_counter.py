import string

file = 'AlicesAdventuresinWonderland_text.txt'
text = open(file, 'r')

word_counts = {}
for line in text:
    data = line.strip().split(' ')  
    for value in data:
        key = value.translate(str.maketrans('','',string.punctuation)).lower()
        if key in word_counts.keys():
            word_counts[key] += 1
        else:
            word_counts.update({key : 1})

print(word_counts)
