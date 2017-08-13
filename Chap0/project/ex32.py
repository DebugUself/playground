# -*- coding: utf-8 -*-

## ex32 循环与列表

# BE 00

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# this first kind of  for-loop goes through a list
for number in the_count:
    print "This is count %d " % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists,first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range (0,6):
    print "Adding %d to the list." % i
    # append is a function that lists inderstand.
    elements.append(i)

# now we can orint thenm out too.
for i in elements:
    print "elements was: %d" % i


# Dk

# 01 range 的用法:
    # **range(4) returns [0, 1, 2, 3]**
    # Return a list containing an arithmetic progression of integers.
    # range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    # When step is given, it specifies the increment (or decrement).
    # For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    # These are exactly the valid indices for a list of 4 elements.

# 02 可以直接赋值 element = [0,1,2,3,4,5]

# 03 列表操作 还有哪些用法?
     # ==> [Python Lists  |  Python Education  |  Google Developers](https://developers.google.com/edu/python/lists) 

     # |  append(...) 向列表尾端添加对象
     # |      L.append(object) -- append object to end
     # |
     # |  count(...)  计算列表中目标 value 的出现次数
     # |      L.count(value) -> integer -- return number of occurrences of value
     # |
     # |  extend(...)  向列表尾端添加列表
     # |      L.extend(iterable) -- extend list by appending elements from the iterable
     # |
     # |  index(...)   查找列表某对象索引号
     # |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
     # |      Raises ValueError if the value is not present.

     # |  insert(...)  在特定索引号的位置插入对象
     # |      L.insert(index, object) -- insert object before index
     # |
     # |  pop(...) 移除目标索引号对应的对象,并返回改对象
     # |      L.pop([index]) -> item -- remove and return item at index (default last).
     # |      Raises IndexError if list is empty or index is out of range.
     # |
     # |  remove(...) 移除第一次出现的某个对象
     # |      L.remove(value) -- remove first occurrence of value.
     # |      Raises ValueError if the value is not present.

     # |  reverse(...) 列表反省
     # |      L.reverse() -- reverse *IN PLACE*
     # |
     # |  sort(...) 从小到大排序
     # |      L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
     # |      cmp(x, y) -> -1, 0, 1