from random import random

print('猜数字游戏，游戏会随机生成一个1-1000的数字，玩家可以多次输入自己猜测的数字，直到猜中为止。')
tag = True
while tag:
    rand = int(random() * 1000 + 1) % 1001
    # print('rand is %d' % rand, type(rand))
    while True:
        guess = input('请输入你猜测的数字：')
        if not guess.isdigit():
            print('请输入正确的数字')
            continue
        guess = int(guess)
        if guess == rand:
            con = input('你猜中了！\n是否继续游戏？(y/n)：')
            if con == 'y':
                break
            else:
                tag = False
                break
        elif guess < rand:
            print('你猜的数字太小了！')
        else:
            print('你猜的数字太大了！')
