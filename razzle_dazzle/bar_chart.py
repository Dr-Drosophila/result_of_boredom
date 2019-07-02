import random
from pprint import pprint

def roll_die( iters ):
    sum = 0
    for i in range( iters ):
        sum += random.randint( 1, 6 )
    return( sum )


list_vals = {}

for i in range( int( input( "Enter number of rounds: " ) ) ):
    number = roll_die(8)
    if number not in list_vals:
        list_vals[number] = 1
    elif number  in list_vals:
        list_vals[number] += 1

pprint( list_vals )
