"""
========= FILE INFORMATION =========================================================
File name:          razzle_dazzle.py
Run using:          python3 razzle_dazzle.py -m <number of games>
Input(s):           <money_start>
Output(s):          -
Description:
    Plays the game of razzle_dazzle

Author:     Chinmay Rele
Date:       2019/04/27
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

import math                     # calculations
import random                   # to roll die
from pprint import pprint       # printing nicely
from collections import Counter # counts thigns
import time
import sys                      # to import a file from the commmand line
import getopt                   # TO PASS IN INPUT AND OUTPUT PARAMETERS
# from scipy.stats import lineregress

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

if __name__ == "__main__":
    string = "python3 razzle_dazzle.py \n\t-m <money_start>"
    try:
        opts, args = getopt.getopt( sys.argv[1:],"hm:",["money_start=",] )
    except getopt.GetoptError:
        print( string )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( string )
            sys.exit()
        elif opt in ("-m", "--money_start"):
            money_start = int(arg)

    print( 'money_start is:\t', money_start )
    print(  )

# a = list( range(10) )
# b = list( range( 0, 18, 2 ) )
# pprint(a)
# pprint(b)
# lineregress( a,b )

# sys.exit()

# rolling the die
#     for razzle_dazzle, the number of iterations should be 8
def roll_die( iters ):
    sum = 0
    for i in range( iters ):
        sum += random.randint( 1, 6 )
    return( sum )

#
#         ,,
#       `7MM             mm
#         MM             MM
#    ,M""bMM   ,6"Yb.  mmMMmm   ,6"Yb.
#  ,AP    MM  8)   MM    MM    8)   MM
#  8MI    MM   ,pm9MM    MM     ,pm9MM
#  `Mb    MM  8M   MM    MM    8M   MM
#   `Wbmd"MML.`Moo9^Yo.  `Mbmo `Moo9^Yo.
#
#

# score board:
#   number that lands on key gets the value as 'reward'
score_board = {
    8:  "100 pts",
    9:  "100 pts",
    10: "50 pts",
    11: "30 pts",
    12: "50 pts",
    13: "50 pts",
    14: "20 pts",
    15: "15 pts",
    16: "10 pts",
    17: "5 pts",
    18: "prize",
    19: "prize",
    20: "prize",
    21: "prize",
    22: "nothing",
    23: "nothing",
    24: "nothing",
    25: "nothing",
    26: "nothing",
    27: "nothing",
    28: "nothing",
    29: "pay double",
    30: "nothing",
    31: "nothing",
    32: "nothing",
    33: "nothing",
    34: "nothing",
    35: "prize",
    36: "prize",
    37: "prize",
    38: "prize",
    39: "5 pts",
    40: "5 pts",
    41: "15 pts",
    42: "20 pts",
    43: "50 pts",
    44: "50 pts",
    45: "30 pts",
    46: "50 pts",
    47: "100 pts",
    48: "100 pts",
}

#
#                            ,,
#                          `7MM
#                            MM
#   ,p6"bo   ,pW"Wq.    ,M""bMM   .gP"Ya
#  6M'  OO  6W'   `Wb ,AP    MM  ,M'   Yb
#  8M       8M     M8 8MI    MM  8M/////
#  YM.    , YA.   ,A9 `Mb    MM  YM.    ,
#   YMbmd'   `Ybmd9'   `Wbmd"MML. `Mbmmd'
#
#

# print( score_board[14] )

# keeps a tab of scores
total_score = 0
num_prizes = 1

price_per_game = 1

num_game = 1

# game; while you still have money
while money_start >= 0:
    score = roll_die( 8 )
    payout = score_board[ score ]
    if "pts" in payout:
        score = int( payout.split()[0] )
        total_score += score
    elif payout == "nothing":
        continue
    elif payout == "prize":
        num_prizes += 1
    elif payout == "pay double":
        price_per_game *= 2

    money_start -= price_per_game
    num_game += 1



    print( "{:>5} :".format( num_game ), end="\t" )
    print( "{:>10} :".format( money_start ), end="\t" )
    print( "score:", score, end="\t" )
    print( "price_per_game: {:>9}".format( price_per_game ), end="\t" )
    print( "payout:", payout )

    if total_score >= 100:
        break

print( "num_prizes:", num_prizes )
print( "total_score:", total_score )
