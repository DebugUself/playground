#filename:python3 10str_int_sum.py
# -*- coding: utf-8 -*-

numbers = "123"#先來一串string
#這個應該先是先做完str轉int后，我自己再增加的，反正是最後添加的
sum0 = 0#這個sum是為了設定sum0 = sum0 + num_int的「起點」
for i in numbers:#來一個高大上的詞，「遞歸」，其實就是做加法，用高逼格的方式把一些東西按**次序**加在一起，或者一個一個進行執行
	num_int = int(i)#「關鍵」的一步，str轉為int：因為只有int才能相加哇，str不好加哇
	sum0 = sum0 + num_int#「關鍵」的一步，int的加法，也是使用「遞歸」的概念：一個一個往上加，而不是我們小學數學里的，一次性加完

print(sum0)#打印出來，答案是6