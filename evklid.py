def evklid(a, b):
    c = 0
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return c

def evklidRec(a, b):
    if a % b == 0:
        return b
    return evklidRec(b, a % b)

