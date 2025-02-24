import sys

def calculator():
    if len(sys.argv) != 3:
        print("Error: Provide two integers as arguments")
        return
    try:
        A = int(sys.argv[1])
    except:
        print("Error: First Argument is not an integer")
        return
    try:
        B = int(sys.argv[2])
    except:
        print("Error: Second Argument is not an integer")
        return
        print("Sum:             =", A+B)
        print("Difference:      =", A-B)
        print("Product:         =", A*B)
    try:
        print("Quotient:        =", A/B)
    except:
        print("Quotient:        =", "ERROR (impossible operation)")
    try:
        print("Remainder:       =", A%B)
    except:
        print("Remainder:       =", "ERROR (impossible operation)")

calculator()