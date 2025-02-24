import sys
import string
#DOC
#Generator expression
#isprintable
#isalpha
#isdigit
#isspace
#isupper
#islower

def text_analyzer(text):
    """ This function takes a text and counts then print
    the number of printable, upper, lower and space character"""
    if text is None:
        print("Error: One string must be provided as argument")
        return
    elif not isinstance(text, str):
        print("Error: Argument must be a string")
        return
    else:
        printable = sum(1 for char in text if char.isprintable())
        upper = sum(1 for char in text if char.isupper())
        lower = sum(1 for char in text if char.islower())
        mark = sum(1 for char in text if char in string.punctuation)
        space = sum(1 for char in text if char.isspace())
        print("The text contains ", printable, " printable character(s)")
        print("- ", upper, " upper letter(s)")
        print("- ", lower, " lower letter(s)")
        print("- ", mark, " punctuation mark(s)")
        print("- ", space, " space(s)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: One string must be provided as argument")
        sys.exit()
    text_analyzer(sys.argv[1])