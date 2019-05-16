"""
========= FILE INFORMATION =========================================================
File name:          isbn_logger.py
Run using:          python3 isbn_logger.py
Input(s):           ISBN (prompted) <filename>
Output(s):          <output>
Description:
    inputs isbns and exports the isbns as a list

Author:     Chinmay Rele
Date:       2019/05/16
Version:    0.0.1

ascii_generator:
    http://patorjk.com/software/taag/#p=display&h=0&v=3&c=bash&f=Georgia11&t=

"""

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

from pprint import pprint
import sys

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

isbn = None
isbn_list = []

while isbn != "done":
    isbn = input( "Enter ISBN or 'done' \n\t" )
    isbn_list.append( isbn )

with open( sys.argv[-1], "w" ) as isbn_file:
    for item in isbn_list:
        print( item, file=isbn_file )

pprint( isbn_list )

#
#                                                ,,
#    mm                                          db
#    MM
#  mmMMmm   .gP"Ya  `7Mb,od8 `7MMpMMMb.pMMMb.  `7MM  `7MMpMMMb.  `7MM  `7MM  ,pP"Ybd
#    MM    ,M'   Yb   MM' "'   MM    MM    MM    MM    MM    MM    MM    MM  8I   `"
#    MM    8M//////   MM       MM    MM    MM    MM    MM    MM    MM    MM  `YMMMa.
#    MM    YM.    ,   MM       MM    MM    MM    MM    MM    MM    MM    MM  L.   I8
#    `Mbmo  `Mbmmd' .JMML.   .JMML  JMML  JMML..JMML..JMML  JMML.  `Mbod"YML.M9mmmP'
#
#
