import random

def generator(text, sep=" ", option=None):
    VALID_OPTION = {"shuffle", "ordered", "unique"}

    if (not isinstance(text, str)):
        print("ERROR")
        return
    elif (not text.isprintable()):
        print("ERROR")
        return
    elif (not isinstance(option, str) or option not in VALID_OPTION):
        print("ERROR")
        return
    s_text = text.split(sep)
    if (option == None):
        for char in s_text:
            yield char
        return
    elif (option == "shuffle"):
        random.shuffle(s_text)
        for char in s_text:
            yield char
        return
    elif (option == "unique"):
        seen = set()
        for char in s_text:
            if char not in seen:
                yield char
        return
    elif(option == "ordered"):
        for char in sorted(s_text):
            yield char
        return