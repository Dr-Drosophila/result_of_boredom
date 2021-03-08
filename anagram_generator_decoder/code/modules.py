def read_in_words( words_file ):
	"""
	- reads in words file
	- returns a list of upper-case words
	"""
	return_lst = []
	with open( words_file, "r" ) as infile:
		for line in infile:
			return_lst.append( line.strip().upper() )
	return( return_lst )

def remove_modifiers( word ):
	"""
	- removes modifiers from a word.
	- returns a list: [ word without modifiers, word with modifiers (original) ]
	"""

	unneeded_chars = [
		'!', '&', "'", ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
	]

	no_mods = word
	for char in unneeded_chars:
		no_mods = no_mods.replace( char, "" )

	return([ no_mods, word ])

def check_subset( lst1, lst2 ):
	"""
	- checks if lst1 is a subset of lst2
	- lst1 should always be smaller/equal than lst2, else fail
	- return bool
	"""

	for char in lst1:
		if char in lst2:
			lst2.remove( char )
		elif char not in lst2:
			return( False )

	return( True )

def remove_word( word, phrase )
