"""
- generates/decodes anagrams
	- Since generating and decoding is the same, we only need to perform a single operation
"""

### imports ==================================================================
from modules import *
from pprint import pprint as pprint

### files ==================================================================
words_file = "/Users/rele.c/Dropbox/RUTGERS/10 - Spring 2019/Quantitative Bio Bioinformatics/result_of_boredom/anagram_generator_decoder/data/raw/words.txt"
phrase = "madonna of the rocks"
# phrase = input("Phrase:")
test_answer = "so dark the con of man"

### code ==================================================================

words_list = read_in_words( words_file )

phrase = [ char for char in phrase.replace(" ", "") ]
for item in words_list:
