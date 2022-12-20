# 1. 定义函数，没有参数的
# def foo():
#     print('function foo')

# foo()

# 2.定义函数，有参数的，实数与形参个数一致
# def foo(x, y):
#     print('function args x=%s y=%s' % (x, y))

# foo(1, 2)
# foo(x=1, y=2)
# foo(y=2, x=1)
# foo(1, y=3)
# foo(x=1, 2) # SyntaxError: positional argument follows keyword argument


# 3.定义函数， 可变位置形参，数据类型是tuple
# def foo(*args):
#     print('function args %s' % str(args), type(args))


# foo()
# foo(1, 2, 3)
# foo(1, x=3) # TypeError: foo() got an unexpected keyword argument 'x'
# foo(*[1, 3, 4, 5])

# 4.定义函数， 可变关键字形参，数据类型是dict
# def foo(**kwargs):
#     print('function foo args %s' % str(kwargs), type(kwargs))


# foo(1)  # TypeError: foo() takes 0 positional arguments but 1 was given
# foo(x=1, y=2, z=3)
# foo(1, x=3) # ypeError: foo() takes 0 positional arguments but 1 was given


# 5. 定义函数，可变位置与可变关键字形参组合使用
# def foo(*args, **kwargs):
#     print('function foo args %s and keyword args %s' %
#           (str(args), str(kwargs)))


# foo(1, 2, x=2, y=4)

# 6.嵌套函数
# def foo():
#     print('run foo')
#     def foo1():
#         print('run foo1')
#     foo1()
# foo()

# 7.函数传参
# def foo1(x, y):
#     print('run foo1 x + y = %d' % (x + y))


# def foo(*args, **kwargs):
#     foo1(*args, **kwargs)


# foo(1, 2)
# foo(1, y=2)
# foo(x=3, y=4)
# foo(1, 2, 3) # TypeError: foo1() takes 2 positional arguments but 3 were given

# 8.装饰器

# import time


# def foo(x, y):
#     time.sleep(3)
#     print('run foo', x, y)


# def wrapper(*args, **kwargs):
#     start = time.time()
#     foo(*args, **kwargs)
#     end = time.time()
#     print('use time', end - start)


# wrapper(1, 2)


# 9.装饰器 优化版
# import time


# def foo(x, y):
#     time.sleep(3)
#     print('run foo', x, y)


# def wrapper(fn):
#     def cb(*args, **kwargs):
#         start = time.time()
#         fn(*args, **kwargs)
#         end = time.time()
#         print('use time', end - start)
#     return cb


# foo = wrapper(foo)

# foo(1, 2)


# 9.装饰器 优化版二
# import time


# def wrapper(fn):
#     def cb(*args, **kwargs):
#         start = time.time()
#         res = fn(*args, **kwargs)
#         end = time.time()
#         print('use time', end - start)
#         return res

#     return cb


# def foo(x, y):
#     time.sleep(2)
#     print('run foo', x, y)
#     return x, y


# foo = wrapper(foo)

# print(foo(1, 2))


# 10.装饰器 优化版三 @ 语法糖  作用：foo = stat_use_time(foo)
# import time


# def stat_use_time(fn):
#     def cb(*args, **kwargs):
#         start = time.time()
#         res = fn(*args, **kwargs)
#         end = time.time()
#         print('use time', end - start)
#         return res

#     return cb

# @stat_use_time
# def foo(x, y):
#     time.sleep(2)
#     print('run foo', x, y)
#     return x, y

# print(foo(1, 2), foo.__name__, foo.__doc__)

# 11.塌饰器 优化版四

from functools import wraps
import time


def stat_use_time(fn):
    @wraps(fn)
    def cb(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        print('use time', end - start)
        return res

    return cb

@stat_use_time
def foo(x, y):
    ''' foo doc '''
    time.sleep(2)
    print('run foo', x, y)
    return x, y

print(foo(1, 2), foo.__name__, foo.__doc__)