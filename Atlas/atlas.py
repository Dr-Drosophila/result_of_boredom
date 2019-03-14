"""
========= FILE INFORMATION =========================================================
File name:			atlas.py
Run using:			python3 atlas.py -t <type_of_game/input_file> -o <sample_game>
Input(s):			-t <type_of_game/input_file>
					-r <random_character>
Output(s):			-o <sample_game>
Description:
	inputs the names of things you want to play with, and outputs a sample game.

Author: 	Chinmay Rele
Date:		2019/03/14
Version:	0.0.01

========= IMPORTS =================================================================
"""

import random # to randomly select items from dictionary values
import sys # to import a file from the commmand line
import getopt # TO PASS IN INPUT AND OUTPUT PARAMETERS
import string

"""
========= FUNCTIONS ===============================================================
"""

## get information from bash
if __name__ == "__main__":
	random_character = 0
	# print( "from main" )
	string = "python3 atlas.py \n\t-t <type_of_game/input_file> \n\t-o <sample_game>\n\t-r <random_character>"
	try:
		opts, args = getopt.getopt( sys.argv[1:],"ht:o:r:",["help", "type_of_game=", "sample_game=", "random_character="] )
	except getopt.GetoptError:
		print( string )
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print( string )
			sys.exit()
		elif opt in ("-t", "--type_of_game"):
			type_of_game = arg
		elif opt in ("-o", "--sample_game"):
			sample_game = arg
		elif opt in ("-r", "--random_character"):
			random_character = arg.upper()

	print( 'type_of_game is:\t', type_of_game )
	print( 'sample_game is:\t\t', sample_game )
	if random_character != 0:
		print( 'random_character is:\t', random_character )

	print(  )

"""
========= CODE ====================================================================
"""

# first, convert the input file to a list
# convert the list to a dictionary of first letters

upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specials = "&- "

# list of items to play with
words = []
# read in all the words to the list
with open( type_of_game, "r" ) as in_file:
	for line in in_file:
		word = line.strip().upper()
		temp_word = None
		for char in word:
			if char not in upper_letters and char not in specials:
				temp_word = word
		if temp_word != None:
			for i in range( len(temp_word) ):
				if temp_word[i] not in upper_letters and char not in specials:
					word = temp_word[:i]
					break
			# print( word )
		words.append( word )

# create dictinary based on starting letter automaticcally
word_dictionary = {}
for word in words:
	if word[0] not in word_dictionary.keys():
		word_dictionary[ word[0] ] = [ word ]
	elif word[0] in word_dictionary.keys():
		word_dictionary[ word[0] ].append(word)

# account for any items that might not be in the dictionary.
for item in upper_letters:
	if item not in word_dictionary.keys():
		word_dictionary[item] = []

# starting condition: random character
if random_character == 0:
	random_character = random.choice( upper_letters )
	print( random_character )

# creating same game
sample_game_lst = [] # add first item directly, and then add to it with a loop
to_add = random.choice( word_dictionary[random_character] )
word_dictionary[random_character].remove( to_add )
sample_game_lst.append( to_add.title() )
random_character = to_add[-1]

while len( word_dictionary[random_character] ) != 0:
	to_add = random.choice( word_dictionary[random_character] )
	word_dictionary[random_character].remove( to_add )
	sample_game_lst.append( to_add.title() )
	random_character = to_add[-1]

[ print( item ) for item in sample_game_lst ]

with open( sample_game, "w" ) as out_file:
	for item in sample_game_lst:
		print( item, file=out_file )
	print( "END", file=out_file )
