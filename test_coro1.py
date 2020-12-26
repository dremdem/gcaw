def add_number(i = 0):
    i = 0
    while True:
        line = yield
        i += 1
        # print(f'{i}: {line}')
        # yield (f'{i}: {line}')
        yield line
           



a = add_number()

next(a)
with open("test.txt", 'r') as f:
    for line in f:
        # a.send(line)
        line_with_number = a.send(line)
        print(line_with_number, end="")

