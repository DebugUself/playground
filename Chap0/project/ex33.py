# -*- coding: utf-8 -*-

## ex33 while 循环

# BE 00



def while_loop(maximum,increment):
    i = 0
    while i < maximum:
        print "At the top i  is %d " % i
        numbers.append(i)

        i += increment
        print "numbers now:",numbers
        print "At the bottom i is %d" % i

def for_range_loop(maximum,increment):
    for i in range(maximum):
        print " i  is %d " % i
        numbers.append(i)
        print "numbers now:",numbers



if __name__ == '__main__':
    numbers = []
    maximum = 10
    increment = 4

    #while_loop(maximum,increment)
    for_range_loop(maximum,increment)
    print "The numbers:"

    for num in numbers:
        print num

#DK
# 01 将循环改成一个函数

# 02 用函数改写脚本,用不同数字测试

# 03 添加增量参数

# 04 使用该函数重写脚本

# 05 for 与 range 重写脚本,不需要递增操作了,若有递增只对第一个数有影响.
    #[increment,increment+1,....,maximum]
