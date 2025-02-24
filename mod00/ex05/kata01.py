import sys

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def write_dic(kata):
    if len(kata) <= 0:
        print("Empty Dictionary")
        return
    for key, value in kata.items():
        print("{}: {}".format(key, value))

write_dic(kata)