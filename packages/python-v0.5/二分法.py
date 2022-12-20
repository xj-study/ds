# 二分查找算法

l = [1, 3, 5, 8, 9, 12, 200, 230, 500, 789, 1000]


# def search(list, target):
#     left, right = 0, len(list) - 1

#     def do_search(left, right):
#         if (left > right):
#             return None
#         mid = left + int((right - left)/2)
#         tmp = list[mid]
#         if tmp == target:
#             return mid
#         elif tmp < target:
#             return do_search(mid + 1, right)
#         else:
#             return do_search(left, mid - 1)

#     res = do_search(left, right)
#     print('%d in list index %s' % (target, str(res)))

def search(find_num, l):
    mid_index = len(l)
    if not mid_index:
        return None
    mid_index = int(mid_index / 2)
    mid = l[mid_index]
    if mid == find_num:
        return mid_index
    elif mid < find_num:
        return search(find_num, l[mid_index+1:])
    else:
        return search(find_num, l[0:mid_index-1])


while True:
    f = input('输入你要查找的数字：')
    f = int(f)
    res = search(f, l)
    print('%d find in %s' % (f, str(res)))
