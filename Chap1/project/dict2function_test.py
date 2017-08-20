#! /usr/bin/env python
# -*- coding: utf-8 -*-

def function0():
    print('0')


def add_comond(command_dict,command_name,commond_func_name):
   # 添加 指令-函数名 到指令字典
    command_name =input("请输入你要添加的指令")
    commond_func_name =input("请输入指令对应执行的函数")
    command_dict[command_name] = commond_func_name
    print(command_dict)

def main():
    command_function_dt = {
        'f0': function0,
    }

    while True:
    # 以字典方式执行指令
        command =input("请输入命令:")
        command_func =command_function_dt.get(command)
        print(command_func)
        command_func()



if __name__ == '__main__':

    main()

