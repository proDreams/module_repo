x = 0
y = 0
op = ''


def init(a, b, c):
    global x, op, y
    x = int(a)
    op = b
    y = int(c)


def calculation():
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y
