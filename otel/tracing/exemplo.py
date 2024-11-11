# Rodar com python -m trace -T exemplo.py

def a():
    # return 28
    return 1/0

def b():
    return a()

def c():
    return b()

def d():
    return c()


print(d())