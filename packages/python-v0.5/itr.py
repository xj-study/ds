# 1.可迭代对象及迭代对象
# 1.1 列表list
# for i in [1,2,3,4]:
#     print(i)
# 1.2 字典dict
# for i in { 'key1':1, 'key2':2, 'key3':3 }:
#     print(i)
# 1.3 字符串str
# for i in 'hello world':
#     print(i)
# 1.4 集合set
# for i in {'a', 'b', 'c'}:
#     print(i)
# 1.5 元组 tuple
# for i in ('a', 'b', 1, 3):
#     print(i)
# 1.6 文件 file
# with open('guess.py', 'rt', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')

# 2.生成式
# 2.1 列表生成式
# l = ['a', 'b', 1, 4]
# print([i for i in l]) # 省略 if判断，默认为True
# print([i for i in l if i == 4]) # if 判断
# print([i*2 for i in l]) # i可以运算
# def parse(i):
#     return i + i
# print([parse(i) for i in l])

# 2.2 字典，集合语法与列表一致，区别就是字典得是键值对
# l = [1, 2, 4, 5]
# print({k: None for k in l})

# 2.3 生成器
# l = [1, 2, 4, 5]
# print(i for i in l)  # <generator object <genexpr> at 0x10b44f510>

# 3.案例 计算一个文件的字符数量
# 3.1 版本一
# with open('guess.py', 'rt', encoding='utf-8') as f:
#     res = 0
#     for line in f:
#         res += len(line)
#     print(res)

# 3.2 版本二，使用列表生成式，若文件行数非常大，就会存在内存溢出问题
# with open('guess.py', 'rt', encoding='utf-8') as f:
#     res = sum([len(line) for line in  f])
#     print(res)

# 3.3 版本三，使用生成器，不存在内存溢出问题
# with open('guess.py', 'rt', encoding='utf-8') as f:
#     res = sum(len(line) for line in f)
#     print(res)
