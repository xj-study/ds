
import demo6
from random import random

# while (1):
#     r = int(random()*101 % 101)
#     c = 0
#     while (1):
#         guess = int(input('请输入您猜测的数字：'))
#         c += 1
#         if guess == r:
#             print('你真棒，猜中了！')
#             break
#         elif guess > r:
#             print('你猜的数字大了')
#         else:
#             print('你猜的数字小了')

#     print(f'您通过{c}次猜中了答案！{r}')
#     isRestart = input('还玩吗？(y/n)：')
#     if isRestart != 'y':
#         break
# print('游戏愉快！')


print('add 10, 20 is', demo6.add(10, 20))
