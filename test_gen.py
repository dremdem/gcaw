
def gen_test1(filename: str) -> str:
    with open(filename, 'r') as f:
        for line in f:
            yield line

gen_test2 = (line for line in open('test.txt', 'r'))


for i in gen_test2:
    print(i, end="")

print(gen_test2)
