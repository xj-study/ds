# 1.全部读取文件，返回str
# with open('guess.py', 'rt', encoding="utf-8") as f:
#     res = f.read()
#     print(type(res))
#     print(res)

# 2.按行全部读取文件，返回list
# with open('guess.py', 'rt', encoding='utf-8') as f:
#     lines = f.readlines()
#     print('lines type', type(lines))
#     for line in lines:
#         print(line, end="")

# 3.一行一行读取，走到全部读取，单选返回str
# with open('guess.py', 'rt', encoding='utf-8') as f:
#     while True:
#         line = f.readline()
#         if line:
#             print(line, end='')
#         else:
#             break

# 4.指定字数读取，返回str
# with open('guess.py', 'rt', encoding='utf-8') as f:
#     while True:
#         line = f.read(20)
#         if line:
#             print(line)
#         else:
#             break
