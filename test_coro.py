def test_coro1():
    pass
    num = (yield)
    for i in range(num):
        print(i)

coro1 = test_coro1()
next(coro1)
coro1.send(5)

