#word distribution graph

import matplotlib
from nltk.corpus import words

#load dictionary
word_list = words.words()

print(len(word_list))

for word in word_list[0:20]:
	print(word)

