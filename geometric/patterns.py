"""
========= FILE INFORMATION =========================================================
File name:          patterns.py
Run using:          python3 patterns.py
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

import turtle
import sys
from turtle import *

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



def rainbow_benzene():
    window = turtle.Screen()
    window.setup(width=2880, height=1800, startx=10, starty=0.5)
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = turtle.Pen()
    turtle.bgcolor('black')
    for x in range(20):
        t.pencolor(colors[x%6])
        # t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
    turtle.hideturtle()
    turtle.penup()
    turtle.getscreen().getcanvas().postscript(file='rainbow_benzene.ps')

def test_drawing():
    wn = Screen()
    alex = Turtle()

    for aColor in ["yellow", "red", "purple", "blue"]:
       alex.color(aColor)
       alex.forward(50)
       alex.left(90)

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


test_drawing()
sys.exit()
rainbow_benzene()


# window = turtle.Screen()
# window.setup(width=2880, height=1800, startx=10, starty=0.5)
# euler = turtle.Turtle()  # A good mathy name for our turtle
# euler.shape("circle")
# euler.speed( 40 )
# scale = 5  # This isn't a turtle module setting.  This is just for us.
#
# # Move the little buddy over to the left side to give him more room to work
# euler.penup()
# euler.setpos(-600, 0)
# euler.pendown()
#
# current = 0   # Here's how we know where we are
# seen = set()  # Here's where we'll keep track of where we've been
#
# # Step increases by 1 each time
# for step_size in range(1, 100):
#
#     backwards = current - step_size
#
#     # Step backwards if its positive and we've never been there before
#     if backwards > 0 and backwards not in seen:
#         euler.setheading(90)  # 90 degrees is pointing straight up
#         # 180 degrees means "draw a semicircle"
#         euler.circle(scale * step_size/2, 180)
#         current = backwards
#         seen.add(current)
#
#     # Otherwise, go forwards
#     else:
#         euler.setheading(270)  # 270 degrees is straight down
#         euler.circle(scale * step_size/2, 180)
#         current += step_size
#         seen.add(current)
#
# # turtle.done()
#
# turtle.getscreen().getcanvas().postscript(file='recaman.ps')


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
