#
#    ,,
#    db                                                    mm
#                                                          MM
#  `7MM  `7MMpMMMb.pMMMb.  `7MMpdMAo.  ,pW"Wq.  `7Mb,od8 mmMMmm  ,pP"Ybd
#    MM    MM    MM    MM    MM   `Wb 6W'   `Wb   MM' "'   MM    8I   `"
#    MM    MM    MM    MM    MM    M8 8M     M8   MM       MM    `YMMMa.
#    MM    MM    MM    MM    MM   ,AP YA.   ,A9   MM       MM    L.   I8
#  .JMML..JMML  JMML  JMML.  MMbmmd'   `Ybmd9'  .JMML.     `Mbmo M9mmmP'
#                            MM
#                          .JMML.

import datetime
from pprint import pprint as pprint
from os import system as bash
import time

#
#      ,...                                           ,,
#    .d' ""                                   mm      db
#    dM`                                      MM
#   mMMmm  `7MM  `7MM  `7MMpMMMb.   ,p6"bo  mmMMmm  `7MM   ,pW"Wq.  `7MMpMMMb.  ,pP"Ybd
#    MM      MM    MM    MM    MM  6M'  OO    MM      MM  6W'   `Wb   MM    MM  8I   `"
#    MM      MM    MM    MM    MM  8M         MM      MM  8M     M8   MM    MM  `YMMMa.
#    MM      MM    MM    MM    MM  YM.    ,   MM      MM  YA.   ,A9   MM    MM  L.   I8
#  .JMML.    `Mbod"YML..JMML  JMML. YMbmd'    `Mbmo .JMML. `Ybmd9'  .JMML  JMML.M9mmmP'
#
#



#
#                            ,,
#                          `7MM
#                            MM
#   ,p6"bo   ,pW"Wq.    ,M""bMM   .gP"Ya
#  6M'  OO  6W'   `Wb ,AP    MM  ,M'   Yb
#  8M       8M     M8 8MI    MM  8M//////
#  YM.    , YA.   ,A9 `Mb    MM  YM.    ,
#   YMbmd'   `Ybmd9'   `Wbmd"MML. `Mbmmd'
#
#

# get timestamp to create file in log
timestamp = str(datetime.datetime.now()).split()

# dictionary that holds data form conversion
data_dict = {}
# characters that can be translated
viable_chars = []

# populate dictionary
with open( "./data/conversion.db", "r" ) as infile:
    for line in infile:
        current_line = line.strip().split("\t")
        data_dict[ current_line[0] ] = [ current_line[1], current_line[2] ]
        viable_chars.append( current_line[0] )

# string that needs to be changed
# query = input("What is your query? \n")
query = "This is a test?"

# handling morse first
temp_to_morse_str = "".join( query.upper().split() )
to_morse_lst = list( temp_to_morse_str )
morse_list = []

for item in to_morse_lst:
    if item in viable_chars:
        morse_list.append( data_dict[item][1] )
        print( data_dict[item][0] )

for item in morse_list:
    for char in item:
        if char == ".":
            bash( "say 'dit'" )

        elif char == "-":
            bash( "say 'do'" )
    time.sleep(0.3)

print( to_morse_lst )
