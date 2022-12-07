'''------列表------'''

print('----------------列表------------------')
lst = [1, 2, 3, 4, 5]
print('列表：', lst)
print('--------------列表-获取----------------')
print('5在列表中的索引：', lst.index(5))
print('in 判断元素是否在列表中：', 5 in lst)
print('not in 判断元素是否在列表中：', 5 not in lst)
print('列表第一项：', lst[0])  # 第一项
# print('列表第一项：', lst[5]) # 超出范围
print('列表最后一项：', lst[-1])  # 最后一项
print('切片获取：', lst[::-1])  # 反转
print('切片获取：', lst[:2:-1])  # 从后面开始
print('切片获取：', lst[:2:1])  # 从前面开始
print('切片获取：', lst[2::1])  # 从前面开始
print('切片获取：', lst[2::-1])  # 从前面开始
print('--------------列表-增加----------------')
lst.append(6)
print('增加一项', lst)
lst.insert(5, 7)
print('插入一项', lst)
lst.extend((8, 9))
print('加入多项', lst)
print('--------------列表-删除----------------')
del lst[1]
print('删除一项', lst)
lst.remove(1)
print('删除一项', lst)

print('--------------列表-修改----------------')
lst[2:5] = []
lst[3] = [2, 3, 4]
lst[1] = 10
print('修改第2项值：', lst)
