# -*- coding: utf-8 -*-

#BE 00

# 引入 argv 模块
from sys import argv
# 参数解包(unpake)
script,input_life = argv
# 定义函数:打印目标文件所有内容
def print_all(f):
    print f.read()
# 定义函数:文件读取指针在目标文件重头读起
def rewind(f):
    f.seek(0)
# 定义函数:打印目标行数以及目标行数对应的内容
def print_a_line(line_count,f):
    print line_count,f.readline()
# 打开目标文件
current_file = open(input_life)
# 给出提示,运行函数:打印脚本所有内容
print "First let's print the whole file:\n"

print_all(current_file)
# 给出提示,运行函数:改变文件读取指针的位置
print "Now let's rewind,kind of like a tape."

rewind(current_file)
# 给出提示,运行函数:打印对应三行
print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line,current_file)

#curent_line = current_line + 1
current_line += 1
print_a_line(current_line,current_file)

# 函数和文件是如何一起发挥作用的?
    # 通过变量传递
# 怎样传递当前行号信息?
    # file.seek(0)

# Dk

## 
