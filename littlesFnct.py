import ast

def turpleToString(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

def stringToDict(string):
    return ast.literal_eval(string)
