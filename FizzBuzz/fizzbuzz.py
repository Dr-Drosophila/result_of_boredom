"""
========= FILE INFORMATION =========================================================
File name:			fizzbuzz.py
Run using:			python3 fizzbuzz.py -n <numbers> -l <total_length_of_game> -o <output_file>
Input(s):			-n <numbers>
					-l <total_length_of_game>
Output(s):			-o <output_file>
Description:
	Plays FizzBuzz

Author: 	Chinmay Rele
Date:		date
Version:	version

========= IMPORTS =================================================================
"""

import sys # to import a file from the commmand line
import getopt # TO PASS IN INPUT AND OUTPUT PARAMETERS

"""
========= FUNCTIONS ===============================================================
"""

## get information from bash
if __name__ == "__main__":
	random_character = 0
	# print( "from main" )
	string = "python3 fizzbuzz.py \n\t-n <numbers; comma seprated numbers> \n\t-l <total_length_of_game> \n\t-o <output_file>"
	try:
		opts, args = getopt.getopt( sys.argv[1:],"hn:l:o:",["help", "numbers=", "total_length_of_game=", "output_file="] )
	except getopt.GetoptError:
		print( string )
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print( string )
			sys.exit()
		elif opt in ("-n", "--numbers"):
			numbers = arg
		elif opt in ("-l", "--total_length_of_game"):
			total_length_of_game = arg
		elif opt in ("-o", "--output_file"):
			output_file = arg.upper()

	print( 'numbers is:\t', numbers )
	print( 'total_length_of_game is:\t\t', total_length_of_game )
	print( 'output_file is:\t', output_file )

	print(  )

"""
========= CODE ====================================================================
"""

# words that fizzbuzz is played by
words = [ "Fizz", "Buzz", "Fooz", "Biff", "Faze", "Booz", "Feet", "Beet", "Fork", "Bork" ]
