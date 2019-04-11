
## ========= IMPORTS =================================================================
import os # import to use os.system

## ========= FUNCTIONS ===============================================================

def bestfun( unphased_out_file ):
    """
    Reads in a file and finds the least p_value
    """
    p_value_file = "p_values.dat"

    # open the input and output files
    with open( unphased_out_file, "r" ) as unphased, open( p_value_file, "a" ) as p_values:
    #     make a lsit of p_vlaues
        p_value_lst = []
    #     append all p_values
        for line in unphased:
            if "p-value" in line:
                p_value_lst.append( float(line.strip().split()[-1]) )
        return min(p_value_lst)


## ========= CODE ====================================================================

# run sumulate first
os.system( "python simulate.py" )
os.system( "" )
