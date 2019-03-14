"""
========= FILE INFORMATION =========================================================
File name:			atlas.py
Run using:			python3 atlas.py -t <type_of_game/input_file> -o <sample_game>
Input(s):			-t <type_of_game/input_file>
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

"""
========= FUNCTIONS ===============================================================
"""

## get information from bash
if __name__ == "__main__":
	# print( "from main" )
	string = "python3 atlas.py \n\t-t <type_of_game/input_file> \n\t-o <sample_game>"
	try:
		opts, args = getopt.getopt( sys.argv[1:],"ht:o:",["help", "type_of_game=", "sample_game="] )
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
			# THE FILE THAT HAS HAS BEEN RUN THROUGH BEDTOOLS MERGE. HAS ALIGNMENT SCORES FOR REPEATS.
			sample_game = arg

	print( 'type_of_game is:', type_of_game )
	print( 'sample_game is:', sample_game )
	print(  )


"""
========= CODE ====================================================================
"""

# first, convert the input file to a list
# convert the list to a dictionary of first letters
