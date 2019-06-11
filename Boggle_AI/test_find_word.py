#test boggle solving algorithm

import numpy as np
import os
#from nltk.corpus import wordnet as wn
from nltk.corpus import words

def check_word(word):
	if word in word_list:
		return word
	else:
		return False

test_list = ['tan','ten','cent','met','men','are','era','uae','monger','rin','dear','dearg','ball','balls']
word_list = words.words()

found_list = []
for w in test_list:
	if check_word(w) != False:
		found_list.append(w)
	else:
		pass

print(found_list)



'''
#print( wn.synsets('would') )
print(words.readme())
# prints 236736
print(len(word_list))
'''