import numpy as np
import sys

#DOC:
#str[start:stop:step]
#argv -> sys.argv
#argc -> len(sys.argv)

def revprint():
    if (len(sys.argv) == 1):
        print("Error: Please provide a string as an Input")
    else:
        str = " ".join(sys.argv[1::])
        print(str[::-1].swapcase())

revprint()