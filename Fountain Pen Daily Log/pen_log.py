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
	print( "{0:>19}\t{1:<36}{2:<36}{3:<15}".format("Date/Time", "Pen", "Ink", "Test/Use" ) )
	print( "-"*108 )
	with open( pen_log, "r" ) as in_file:
		for line in in_file:
			line = line.strip().split("\t")
			print( "{0:>19}\t{1:<36}{2:<36}{3:<15}".format( line[0], line[1], line[2], line[3] ) )
	print(  )

# checks notes for selected pen
def check_notes( pen_log ):
	pens_dict = {}
	i = 1
	with open( pen_log, "r" ) as in_file:
		for line in in_file:
			line = line.strip().split("\t")
			temp = line[0][:10] + " == " + line[1] + " == " + line[2]
			pens_dict[i] = [ temp, line[4] ]
			i += 1
	print(  )
	for key, val in pens_dict.items():
		print( key, "\t", val[0] )
	number = int( input( "Which pen do you want information about? " ) )
	print()
	print( pens_dict[ number ][0] )
	print( "\t" + pens_dict[ number ][1] )
	print()


## get information from bash
if __name__ == "__main__":
	# print( "from main" )
	string = "python3 game.py \n\t-i <input_log> \n\t-c (<check_log>)\n\t\n\t-n (check notes for pen in index)"
	try:
		opts, args = getopt.getopt( sys.argv[1:],"hi:cn",["help", "input_log=", "check_log", "notes_check"] )
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
		elif opt == "-n":
			check_notes( input_log )
			sys.exit(0)

	print( 'input_log is:\t', input_log )
	print(  )

"""
========= CODE ====================================================================
"""

# requestiung user data
date_time = str( datetime.datetime.now() )[:19]
pen = input( "Brand/Model of Pen (Nib):\t" ).title()
ink = input( "Ink:\t\t\t\t" ).title()
test_use = input( "Testing or Using?\t\t" ).title()
notes = input( "Notes: " ).capitalize()

# if no notes, then notes = "N/A" to maintain tabs in file
if notes == "":
	notes = "N/A"

# list of things that need proper capitalizations
cap_list = {
	"Fpr"	: "FPR", 	# Fountain Pen Revolution
	"Vp"	: "VP",		# Vanishing Point (Pilot)
	"Rk"	: "R&K",	# Rohrer und Klingner
	"Sb"	: "SB",		# Soft Broad (nib designation)
	"Uef"	: "UEF",	# Ultra Extra Fine (nib designation)

	"Na"	: "N/A"		# Not Applicable
}

# checking if i need to change something in the name.
for key, val in cap_list.items() :
	if key in pen:
		pen = pen.replace( key, val )
	if key in ink:
		ink = ink.replace( key, val )

pen_info = [
	date_time,
	pen,
	ink,
	test_use,
	notes
]

# print( log_print(input_log) )

# writing to the output file
with open( input_log, "a" ) as out_file:
	print(  )
	print( "-"*108 )
	print( "-"*108 )
	print(  )
	print( "{0:>19}\t{1:<36}{2:<36}{3:<15}\n".format( "Time", "Pen", "Ink", "Test/Use" ) )
	print( "{0:>19}\t{1:<36}{2:<36}{3:<15}\nNotes: \t{4}".format( pen_info[0], pen_info[1], pen_info[2], pen_info[3], pen_info[4] ) )
	print( "\t".join( pen_info ), file=out_file )
	print( "\n\tAdded information.\n" )
