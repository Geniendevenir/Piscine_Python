import sys
import string

MORSE = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-...",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    " ":"/"
}

def write_morse():
    if len(sys.argv) <= 1:
        print("Error: Needs at least one arguments")
    text = " ".join(sys.argv[1::])
    for char in text:
        if char not in string.ascii_letters and char not in string.digits and char not in string.whitespace:
            print("Error: Only Space and alpagnumeric are allowed")
            return
    u_text = text.upper()
    for char in u_text:
            print(f'{MORSE[char]} ', end="")
write_morse()