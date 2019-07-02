"""
========= FILE INFORMATION =========================================================
File name:          geometric.py
Run using:          python3 geometric.py
Input(s):
Output(s):
Description:
    Creates geometric patterns.


Author:     Chinmay Rele
Date:       2019/06/16
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

from turtle import *
import turtle
import random

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

screen = Screen()
screen.screensize( 2880, 1800, "black" )

pen = Pen()
pen.speed( 3000 )

size = 20

for i in range( 150 ):
    r = random.randint( 0, 255 )
    g = random.randint( 0, 255 )
    b = random.randint( 0, 255 )

    randcol = ( r, g, b )
    colormode( 255 )

    pen.color( randcol )
    pen.circle( size, steps = 3 )
    pen.right( 11 )

    size += 3

turtle.getscreen().getcanvas().postscript(file='outputname.ps')

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
