"""
========= FILE INFORMATION =========================================================
File name:			game.py
Run using:			python3 game.py -t <type_of_game/input_file> -o <sample_game>
Input(s):			-t <type_of_game/input_file>
					-r <random_character>
Output(s):			-o <sample_game>
Description:
	Inputs the name of the game you want to play, and then starts asking you for the next word.
	This is like a normal game.

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
	string = "python3 game.py \n\t-t <type_of_game/input_file> \n\t-o <sample_game>\n\t-r <random_character>\n\n\tTo check if an item has already been said: while entering item name, put '-c' and then the name of the item."
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

def write_to_file( file):
	with open( file, "w" ) as out_file:
		for item in sample_game_lst:
			print( item, file=out_file )
		print( "END", file=out_file )

def print_list( lst ):
	longest = 0
	for item in lst:
		if len(item) > longest:
	 		longest = len(item)
	print(longest)
	temp_words = []
	for item in lst:
		item += " "
		while len( item ) < longest + 1:
			item += "-"
		item += ">"
		temp_words.append(item)

	table = []
	[ table.append( temp_words[i:i+4] ) for i in range( 0, len(temp_words), 4 ) ]

	for item in table:
		while len(item) < 4:
			item.append( " " )
		print( "{0:<33}{1:<33}{2:<33}{3:<33}".format(item[0], item[1], item[2], item[3]) )




"""
========= CODE ====================================================================
"""

print( "Welcome to the game.\n\tMake sure that you type the name of the %s correctly."%type_of_game )
print()

# first, convert the input file to a list
# convert the list to a dictionary of first letters

upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specials = "&- "
if random_character == 0:
	random_character = random.choice( upper_letters )

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

# creating same game
sample_game_lst = [] # add first item directly, and then add to it with a loop
to_add = random.choice( word_dictionary[random_character] )
word_dictionary[random_character].remove( to_add )
sample_game_lst.append( to_add.title() )
random_character = to_add[-1]

while len( word_dictionary[random_character] ) != 0:
	for i in range( len(words) ):
		if i % 2 == 0:
			to_add = random.choice( word_dictionary[random_character] )
			word_dictionary[random_character].remove( to_add )
			sample_game_lst.append( to_add.title() )
			random_character = to_add[-1]
			# print( "\t\t\t\t\t\t\t\t%s"%sample_game_lst[-1] )
		elif i % 2 != 0:
			print_list( sample_game_lst )
			print()
			usr_input = input( "Input your _%s_ name: "%type_of_game.split(".")[0] )
			if usr_input[0:2] == "-c":
				to_add = usr_input.upper()[3:]
			elif usr_input[0:2] != "-c":
				to_add = usr_input.upper()
				print( )
			if to_add[0] != random_character:
				print( "\n\tWrong starting letter!\n\tYou lose.\n" )
				write_to_file( sample_game )
				sys.exit(0)
			if usr_input.title() in sample_game_lst:
				print( "\n\tAlready said.\n\tYou lose.\n" )
				write_to_file( sample_game )
				sys.exit(0)
			word_dictionary[to_add[0]].remove( to_add )
			random_character = to_add[-1]
			sample_game_lst.append( usr_input.title() )

[ print( item ) for item in sample_game_lst ]
