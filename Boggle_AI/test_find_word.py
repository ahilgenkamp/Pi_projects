#test boggle solving algorithm
#https://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver

import numpy as np
import os
#import networkx as nx
import matplotlib.pyplot as plt
#from nltk.corpus import wordnet as wn
from nltk.corpus import words

#load dictionary
word_list = words.words()

def check_word(word):
	if word in word_list:
		return word
	else:
		return False

boggle_board = [
					['t','n','t','i','l'],
					['e','c','a','i','d'],
					['m','o','n','g','e'],
					['f','i','i','r','a'],
					['a','a','g','b','u']
				]


def extend_path(path, min_len=3, max_len=5):
	i = path[0]
	j = path[1]
	word = boggle_board[i][j]
	if len(word) < max_len:
		for x, y in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]:
				return word+boggle_board[i+x][j+y]
	else:
		return word		
	


print(extend_path(path=(0,0)))

'''
answer_list = []
for i in range(2): #len(boggle_board)
	for j in range(2): #len(boggle_board[i])
		for x, y in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]:
			try:
				print(boggle_board[i][j]+boggle_board[i+x][j+y])
			except:
				pass
'''

'''
for wlen in range(3,max_word_len+1):
	for i in range(len(boggle_board)):	
		for j in range(len(boggle_board[i])):
			if j+wlen < len(boggle_board[i])+1:
				potential_word = ''.join(boggle_board[i][j:j+wlen])
				if check_word(potential_word) is not False:
					answer_list.append(potential_word)
				else:
					pass
			else:
				pass

print(answer_list)
'''


'''
test_list = ['tan','ten','cent','met','men','are','era','uae','monger','rin','dear','dearg','ball','balls']
#does not seem to capture plurals of words...

found_list = []
for w in test_list:
	if check_word(w) != False:
		found_list.append(w)
	else:
		pass

print(found_list)
'''


'''
#print( wn.synsets('would') )
print(words.readme())
# prints 236736
print(len(word_list))
'''


'''
#use networkx and create neighbors for numbers.  that allows you to traverse
G = nx.Graph()

#add all nodes
for i in range(len(test_boggle_board)):
	for j in range(len(test_boggle_board[i])):
		G.add_node(test_boggle_board[i][j])
		#try to add edge behind diagionally
		try:
			G.add_edge(test_boggle_board[i-1][j-1],test_boggle_board[i][j])
		except:
			pass
		#try to add edge behind in the same column
		try:
			G.add_edge(test_boggle_board[i-1][j],test_boggle_board[i][j])
		except:
			pass
		#try to add edge behind in the same row
		try:
			G.add_edge(test_boggle_board[i][j-1],test_boggle_board[i][j])
		except:
			pass

#nx.draw(G, node_size = 10, with_labels=True)
#plt.show()
print(nx.info(G))

'''
