# -*- coding:utf-8 -*-

# BE 00

from sys import argv

script,user_name,user_key = argv
prompt = '$'

print "Hi %s, I'm the %s script." % (user_name,script)
print "your key is %s" % user_key
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computor do you have?"
computor = raw_input(prompt)

print"""
Alright,so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computor. Nice.
""" % (likes,lives,computor)

# DK
# 01 玩 Zork Adventure 文字游戏

# 02 将">"改成"$"

# 03 添加使用参数 user_key
