import random
import sys
from sys import exit

# 生成4位随机数列(可能首位为0)
def random_list_build():
    random_list = []
    random_list = random.sample(range(10),4)
    return random_list

# 修正首位为0的随机数列
def random_list_check(random_list):

    if random_list[0] == 0:
        random_list = random.sample(range(1,10),4)
        print("随机数列满足要求!生成成功!")
    else:
        print("随机数列满足要求!生成成功!")

    return random_list


# 将4位随机数列转化成一个随机数
# def random_number_build(random_list):
#     random_number = random_list[0]*1000 + \
#                     random_list[1]*100  + \
#                     random_list[2]*10   + \
#                     random_list[3]*1

#     print ("随机数生成成功!")
#     return random_number

# 将用户输入转化成 int 数列
def input_number_deal():
    input_str = input("请输入您猜的4位数字,如'1234': ")
    input_list = []

    if len(input_str) != 4: 
        input_str = input("请重新输入,确认输入的是4位数字: ")
    else:
        pass

    input_strlist = list(input_str)
    input_number = int(input_str)
    input_list = list(map(int, input_strlist))


    return input_list


# 比较 随机数列 与 输入数列,给出 AB 结果,当 4A 时退出游戏.
def compare(random_list,input_list):

    A_count = 0
    B_count = 0
    
    # A,B的判定
    for i in range(0,4):
        if random_list[i] == input_list[i]:
            A_count += 1
        else:
            pass

        if random_list[i] in input_list:
            B_count += 1
        else:
            pass

    print (A_count,"A",B_count,"B")

    if A_count == 4:
        print ("猜对了! Bye~")
        exit(0)
# 机会计数
def chance_count(try_number):

    chance_number = 10 - try_number
    print ("你还有 %d 次机会" % chance_number)

# 主函数:随机数列/判断互动/机会计数
def main():

    # 游戏提示
    print('''
        猜数字游戏:
        - 程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
        - 用户输入 4 位数进行猜测，程序返回相应提示
        - 用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
        - 比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
        - 猜对或用完 10 次机会，游戏结束
        祝你好运~
        ''')
    # 处理随机数列
    random_list = random_list_build()
    random_list = random_list_check(random_list)

    try_number = 0
    # 进入互动
    while True:
        # 处理输入数列
        input_list = input_number_deal()

        # 在机会次数下,执行比较与互动,同时机会计数,
        if try_number < 9:
            compare(random_list,input_list)
            try_number += 1
            chance_count(try_number)
        # 机会用完
        elif try_number == 9:
            print ("对不起,机会已经用完")
            break

        else:
            print ("发生错误")
            break


if __name__ == '__main__':
    main()
    #random_number = random_number_build(random_list)
    #input_number_deal()


name

