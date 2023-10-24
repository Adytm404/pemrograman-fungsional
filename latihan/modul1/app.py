def minus (a, b):
    return a - b 

def mult (a, b):
    return a * b 

def add (a, b):
    return a + b

def div (a, b):
    return a / b 

def expression_tree (a, b, c, d):
    return mult(add(a, b), minus(c, d))

print("Hasil evaluasi pohon ekspersi: ", expression_tree(2, 3, 5, 1))