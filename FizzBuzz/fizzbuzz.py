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
			total_length_of_game = int(arg)
		elif opt in ("-o", "--output_file"):
			output_file = arg

	print( 'numbers is:\t\t', numbers )
	print( 'total_length_of_game is:', total_length_of_game )
	print( 'output_file is:\t\t', output_file )

	print(  )

"""
========= CODE ====================================================================
"""

# words that fizzbuzz is played by
# 	need to add more to accomodate more numbers
words = [ "Fizz", "Buzz", "Fooz", "Biff", "Faze", "Booz", "Feet", "Beet", "Fork", "Bork" ]

temp_nums = numbers.split(",")
numbers = []
[ numbers.append(int(item)) for item in temp_nums ]

# create ductionary of numbers and words
num_dict = {}
for i in range( len(numbers) ):
	num_dict[ numbers[i] ] = words[i]

print( num_dict )

output_lst = []

## for loop to create the output:
# for i in range( 1, total_length_of_game+1 ):
# 	thing = ""
# 	for item in list( num_dict.keys() ):
# 		if i % item == 0:
# 			thing += num_dict[item]
# 	if thing == "":
# 		thing = str(i)
# 	output_lst.append( thing )

# print( output_lst )

with open( output_file, "w" ) as out_file:
	for key, val in num_dict.items():
		print( "{0}: {1}".format( key, val ), file=out_file )
	print( "len(game) = " + str(total_length_of_game), file=out_file )
	print( file=out_file )
	for i in range( 1, total_length_of_game+1 ):
		thing = ""
		for item in list( num_dict.keys() ):
			if i % item == 0:
				thing += num_dict[item]
		if thing == "":
			thing = str(i)
		print( thing, file=out_file )
	for item in output_lst:
		print( item, file=out_file )
