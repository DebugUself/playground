# -*- coding: utf-8 -*-

## BE 00

people = 30
cars = 40
buses = 15



if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "we still can't decide."

if people > buses:
    print "Alright,let's just take the buses."
else:
    print"Fine,let's stay home then."



# DK

# 01 
# 其实都和 if 差不多,执行条件判断,elif 的作用:开启新的条件分支,继续往下;else :余下所有部分,跳出if;
