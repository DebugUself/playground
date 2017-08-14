import random
import sys
from sys import exit


# 计算并提示玩家剩余的机会次数
def chance_count(try_number):

    chance_number = 10 - try_number
    print ("你还有 %d 次机会" % chance_number)


# 比较随机数与输入数的大小并给出提示
def number_compare(random_number,input_number):

    if random_number > input_number:
        print ("小了")

    elif random_number < input_number:
        print ("大了")

    elif random_number == input_number:
        print ("对了! Bye~")
        exit(0)

    else:

        print ("发生了一些错误")


# 主运行程序
def try_count(random_number):

    try_number = 0

    while True:
        input_number = input("请输入您要猜测的数字:")
        input_number = int(input_number)

        # 如果 尝试次数小雨10,则执行比较,计数,
        if try_number < 9:
            number_compare(random_number,input_number)
            chance_count(try_number)
            try_number += 1

        elif try_number == 9:
            print ("对不起,机会已经用完")
            break

        else:
            print ("发生错误")
            break
            


if __name__ == '__main__':
    print('''
        猜数字游戏:
        你有 10 次机会来猜测
        计算机生成的(0,20)内随机数的数值
        祝你好运~
        ''')
    # 随机给出给[0,21)内的一个整数
    random_number = random.randrange(21)
    print("随机数已生成!")

    try_count(random_number)