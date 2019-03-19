"""
========= FILE INFORMATION =========================================================
File name:			pen_log.py
Run using:			python3 pen_log.py
Input(s):			-c <check log>
					-i <input file>
					Upon prompt, will need pen and ink information
Output(s):			no output unless requested( print only )
					input file rewritten
Description:
	Logs foutnain pen usage with ink

Author: 	Chinmay Rele
Date:		2019/03/18
Version:	0.0.01

========= IMPORTS =================================================================
"""

import random # to randomly select items from dictionary values
import sys # to import a file from the commmand line
import getopt # TO PASS IN INPUT AND OUTPUT PARAMETERS
import string
import datetime

"""
========= FUNCTIONS ===============================================================
"""

# print the log of pens
def log_print( pen_log ):
	print(  )
	print( "{0:>26}\t{1:<36}{2:<36}{3:<15}".format("Date/Time", "Pen", "Ink", "Test/Use" ) )
	print( "-"*120 )
	with open( pen_log, "r" ) as in_file:
		for line in in_file:
			line = line.strip().split("\t")
			print( "{0:>26}\t{1:<36}{2:<36}{3:<15}".format( line[0], line[1], line[2], line[3] ) )
	print(  )

## get information from bash
if __name__ == "__main__":
	# print( "from main" )
	string = "python3 game.py \n\t-i <input_log> \n\t-c (<check_log>)\n\t"
	try:
		opts, args = getopt.getopt( sys.argv[1:],"hi:c",["help", "input_log=", "check_log"] )
	except getopt.GetoptError:
		print( string )
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print( string )
			sys.exit()
		elif opt in ("-i", "--input_log"):
			input_log = arg
		elif opt == "-c":
			log_print( input_log )
			sys.exit(0)

	print( 'input_log is:\t', input_log )
	print(  )

"""
========= CODE ====================================================================
"""

date_time = str( datetime.datetime.now() )
pen = input( "Brand/Model of Pen (Nib):\t" ).title()
ink = input( "Ink:\t\t\t\t" ).title()
test_use = input( "Testing or Using?\t\t" ).title()

pen_info = [
	date_time,
	pen,
	ink,
	test_use
]

print( log_print(input_log) )

with open( input_log, "a" ) as out_file:
	print( "{0:>26}\t{1:<36}{2:<36}{3:<15}".format( pen_info[0], pen_info[1], pen_info[2], pen_info[3] ) )
	print( "\t".join( pen_info ), file=out_file )

print( "\n\tAdded information.\n" )
