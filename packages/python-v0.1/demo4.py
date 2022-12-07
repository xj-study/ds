def add(x, y):
    return x+y


rst = add(1, 2)
print('1 + 2 =', rst)

rst = add(*[1, 2])
print('list 1 + 2 =', rst)

d = {'x': 4, 'y': 5}
rst = add(**d)
print('map 1 + 2 =', rst)


def foo(**args):
    print(args)


def foo2(*args):
    print(args)


foo(a=1, b=2)
foo2(1, 2, 34, 'ab', 'c')
