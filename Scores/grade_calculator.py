"""
========= FILE INFORMATION ==========================================================
File name:			grade_calculator.py
Run using:			python3 grade_calculator.py -a <assignment> -s <your score> -m <max score>
Input(s):			-a <assignment>
					-s <your score>
					-m <max score>
					scores.tab (internal)
Output(s):			print statement(s)
					scores.tab (internal)
Argument(s):		-c
					-r
Author: 			Chinmay Rele
Version:			0.00.02 (2019/03/07)
					0.00.01 (2019/03/06)

Description:
	Asks for assignment name (single string (no space)), your score and the max score, and calcualtes percentage based on all previous assignments also.
		NOTE:	IMPORANT TO HAVE THE scores.tab file IN THE SAME DIRECTORY


Version History:

0.0.1			Basic version
				Contains: { -a, -s, -m, -r, -c }

0.0.2			Added multiple remove (by index; requests input)

========= IMPORTS ==================================================================
"""

import sys # to import a file from the commmand line
import getopt # TO PASS IN INPUT AND OUTPUT PARAMETERS
from Bio import SeqIO # Need Seq.IO for parsing and making FASTA file
import collections # TEMP TO SEE IF THERE ARE REPEATS IN ANY LISTS
import re # USED TO SPLIT STRINGS TO SEPARATE THE NAME AND ALIGNMENT OF THE REPEATMASKER LIBRARY ANNOTATION.
import math # for absolute method
import random # for random choice
import decimal

"""
========= FUNCTIONS ================================================================
"""
class score( object ):
	"""score utilities"""
	def just_check():
		"""
		Just checks scores and exits
		"""
		all_scores = []
		with open( "scores.tab", "r" ) as scores:
			for line in scores:
				temp = line.strip().split("\t")
				score = []
				score.append( temp[0] )
				score.append( float(temp[1]) )
				score.append( float(temp[2]) )
				all_scores.append( score )
		all_scores = sorted( all_scores )
		print( "{0:^21}|{1:^12}|{2:^12}".format("Assignment Name", "Grade", "Max Score") )
		print("=============================================")
		for item in all_scores:
			print( "{0:>20} |{1:^12}|{2:^12}".format(item[0], item[1], item[2]) )
		print("=============================================")
		score_sum = 0.0
		max_score_sum = 0.0
		for item in all_scores:
			score_sum += item[1]
			max_score_sum += item[2]
		print( "{0:^21}|{1:^12}|{2:^12}".format("Total", score_sum, max_score_sum) )
		print( "{0:^21}|{1:^12}|{2:^12}".format("Percent", round(score_sum/max_score_sum*100, 2), (max_score_sum/max_score_sum*100)) )
		sys.exit()

	def remove():
		all_scores = []
		with open( "scores.tab", "r" ) as scores:
			for line in scores:
				temp = line.strip().split("\t")
				score = []
				score.append( temp[0] )
				score.append( float(temp[1]) )
				score.append( float(temp[2]) )
				all_scores.append( score )
		all_scores = sorted( all_scores )
		for i in range( len(all_scores) ):
			print( i , "\t:\t", all_scores[i] )

		nums = input('Enter the index of the item you want to delete: ')
		items = nums.split(",")
		indeces = []
		[ indeces.append(int(item)) for item in items ]
		indeces.sort( reverse=True )
		for item in indeces:
			indx = int(item)
			del all_scores[indx]

		with open( "scores.tab", "w" ) as score_file:
			for item in all_scores:
				print( "\t".join([ item[0], str(item[1]), str(item[2]) ]), file=score_file )


if __name__ == "__main__":
	error_message = "\n python3 grade_calculator.py \n\t -a <assignment> (name of the assignment; no spaces) \n\t -s <your_score> \n\t -m <max_score>\n\t -c (no argument; no addition of scores; only checks) \n\t -r (no argument, help shown; removes the assignment)\n"
	try:
		opts, args = getopt.getopt( sys.argv[1:],"ha:s:m:cr",["help", "assignment=", "your_score=", "max_score=", "check", "remove"] )
	except getopt.GetoptError:
		print( error_message )
		print(getopt.GetoptError)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print( error_message )
			sys.exit()
		elif opt == "-c":
			score.just_check()
			sys.exit()
		elif opt == "-r":
			score.remove()
			print()
			score.just_check()
			sys.exit()
		elif opt in ("-a", "--assignment"):
			assignment = arg
		elif opt in ("-s", "--your_score"):
			your_score = arg
		elif opt in ("-m", "--max_score"):
			max_score = arg
	print(  )
	print( 'Current Assignment is:\t', assignment )
	print( 'Current Score is:\t', your_score )
	print( 'Current Max Score is:\t', max_score )
	print(  )

"""
========= CODE =====================================================================
"""

# read in the scores.tab file into a list
all_scores = []
with open( "scores.tab", "r" ) as scores:
	for line in scores:
		temp = line.strip().split("\t")
		score = []
		score.append( temp[0] )
		score.append( float(temp[1]) )
		score.append( float(temp[2]) )
		all_scores.append( score )
all_scores = sorted( all_scores )

# stores current score as a list
current_score = []
current_score.append( assignment )
current_score.append( float(your_score) )
current_score.append( float(max_score) )

# boolean for append
to_append = True
# for each item, check for duplicates with current_score
for i in range( len(all_scores) ):
	for item in all_scores:
		# check name and max_score of assignment
		if item[0] == current_score[0] and item[2] == current_score[2]:
			all_scores.remove( item )
			# remove duplicate
			write = False
all_scores.append( current_score )

# formatting; structure courtesy of {Hansen, W}
print( "{0:^21}|{1:^12}|{2:^12}".format("Assignment Name", "Grade", "Max Score") )
print("=============================================")
for item in all_scores:
	print( "{0:>20} |{1:^12}|{2:^12}".format(item[0], item[1], item[2]) )
print("=============================================")

# calculate score and percentages; print to screen
score_sum = 0.0
max_score_sum = 0.0
for item in all_scores:
	score_sum += item[1]
	max_score_sum += item[2]
print( "{0:^21}|{1:^12}|{2:^12}".format("Total", score_sum, max_score_sum) )
print( "{0:^21}|{1:^12}|{2:^12}".format("Percent", round(score_sum/max_score_sum*100, 2), (max_score_sum/max_score_sum*100)) )

if to_append:
	with open( "scores.tab", "a" ) as score_file:
		print( "\t".join([ current_score[0], str(current_score[1]), str(current_score[2]) ]), file=score_file )

# checking for internal duplicates (same name; different scores)
ass_list = []
for item in all_scores:
	ass_list.append( item[0] )

repeat = []
for item in ass_list:
	if ass_list.count(item) > 1:
		repeat.append( item )

repeat = list(set(repeat))
for item in repeat:
	print("\n\nWARNING!!!\n\n\t%s has multiple occurances. \n\tUse -r to remove.\n\tRe-add the line using -a <assignment> -s <your_score> -m <max_score>\n\n\tFor help, use -h\n" %item)
