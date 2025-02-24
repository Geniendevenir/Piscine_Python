import numpy as np
import argparse
import sys
#DOC:
#try/except When attempting a dangerous opperation to avoid crashes
#isinstance(variable, type) to check if a variable is of the type provided

def whois():
    if len(sys.argv) <= 1:
        return print("Error: Please provide an integer as an argument")
    elif len(sys.argv) > 2:
        return print("Error: More than one Argument provided")
    try:
        nbr = int(sys.argv[1])
    except:
        return print("Error: Provided Argument must be an int")
    if nbr == 0:
        return print("I'm Zero.")
    elif nbr % 2 == 0:
        return print("I'm Even.")
    else:
        return print("I'm Odd.")

whois()