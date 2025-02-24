import sys
import string

def ft_filter():
    if len(sys.argv) != 3:
        print("Error: Must enter 3 arguments")
    text = sys.argv[1].split(" ")
    number = int(sys.argv[2])
    print('[', end="")
    for w in text:
        w_ponct = sum(1 for char in w if char in string.punctuation)
        if len(w) > number:
            w_sup = "".join(char for char in w if char not in string.punctuation)
            print(f'\'{w_sup}\', ', end="")
    print(']')
ft_filter()




