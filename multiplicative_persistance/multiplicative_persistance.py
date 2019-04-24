
#
# `7MMpMMMb.pMMMb.          `7MMpdMAo.  .gP"Ya  `7Mb,od8
#   MM    MM    MM            MM   `Wb ,M'   Yb   MM' "'
#   MM    MM    MM            MM    M8 8M""""""   MM
#   MM    MM    MM            MM   ,AP YM.    ,   MM
# .JMML  JMML  JMML.          MMbmmd'   `Mbmmd' .JMML.
#                             MM
#                   mmmmmmm .JMML.

"""
========= FILE INFORMATION =========================================================
File name:           multiplicative_persistance.py
Run using:           python3 multiplicative_persistance.py
Input(s):           <number>
Description:
    finds the multiplicative persistance of a number.
    https://www.youtube.com/watch?v=E4mrC39sEOQ

Author:     Chinmay Rele
Date:        2019/04/24
Version:    0.0.1

ascii_generator:
    http://patorjk.com/software/taag/#p=display&h=0&v=3&c=bash&f=Georgia11&t=
========= IMPORTS =================================================================
"""

import sys

"""
========= FUNCTIONS ===============================================================
"""

def m_persistance( num, steps = 0 ):
    if len( str(num) ) == 1:
        print( "total_steps:", steps )
        return( steps )


    steps += 1
    digits = [ int(i) for i in str( num ) ]

    result = 1
    for i in digits:
        result *= i

    print( "{0:>3}: {1}".format(steps, result) )
    m_persistance( result, steps )

def a_persistance( num, steps = 0 ):
    if len( str(num) ) == 1:
        print( "total_steps:", steps )
        return( steps )


    steps += 1
    digits = [ int(i) for i in str( num ) ]

    result = 0
    for i in digits:
        result += i**2

    print( "{0:>3}: {1}".format(steps, result) )
    a_persistance( result, steps )


"""
========= CODE ====================================================================
"""

m_persistance( int(input( "Input number (mult): " )) )
a_persistance( int(input( "Input number (add): " )) )
