#word distribution graph

import string
import matplotlib
from nltk.corpus import words

#load dictionary
word_list = words.words()

print('Total Words: '+str(len(word_list)))

low = string.ascii_lowercase
'''
for i in range(len(low)):
	num_letters = sum(a.lower() == low[i] for a, *_ in word_list)  #for notes on *_  --> https://www.python.org/dev/peps/pep-3132/
	print(low[i].upper()+': '+str(num_letters))
'''
two_letters = []
for i in low:
	for j in low:
		two_letters.append(i+j)

for i in range(len(two_letters[0:35])):
	num_letters = sum(a[0:2].lower() == two_letters[i] for a in word_list)  #for notes on *_  --> https://www.python.org/dev/peps/pep-3132/
	print(two_letters[i].upper()+': '+str(num_letters))
