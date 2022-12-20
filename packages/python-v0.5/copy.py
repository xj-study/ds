# 复制文件
from re import T


tarsrc = input('请输入要复制的文件：')
distsrc = input('复制的文件路径：')
with open(tarsrc, 'rt', encoding='utf-8') as f, open(distsrc, 'wt', encoding='utf-8') as f1:
    while True:
        l = f.read(100)
        if l:
            f1.write(l)
        else:
            break
    print('复制成功')
