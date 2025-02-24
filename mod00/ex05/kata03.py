import sys

kata = ""

def display_42(kata):
    print(f'{"*" * (42 - len(kata))}{kata}', end="")
display_42(kata)