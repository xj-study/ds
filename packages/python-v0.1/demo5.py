'''------字典------'''

print('----------------字典------------------')
dct = {'a': 1, 'b': 2}
print('字典：', dct)
print('--------------字典-获取----------------')
print('in 判断元素是否在字典中：', 5 in dct)
print('not in 判断元素是否在字典中：', 5 not in dct)
print('字典a：', dct.get('a'))
print('字典b：', dct['b'])
print('字典：', dct.keys())
print('字典：', dct.values())
print('字典：', dct.items())
# print('--------------字典-增加----------------')
dct.update(c=3, e=9)
dct.update({'d': 4, 'f': 8})
print('字典：', dct)


d1 = {'a': 2, 'b': 3}
# print('--------------字典-删除----------------')
dct.pop('a')
print('字典：', dct)

item = dct.popitem()
print('字典：', item)

dct.clear()
print('字典clear：', dct)
