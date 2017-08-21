#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests

r = requests.get('https://api.github.com/events') #<Response [200]>
print(r)

r = requests.post('http://httpbin.org/post',data = {'key':'value'} )
print(r)

r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print(r)
r = requests.delete('http://httpbin.org/delete')
print(r)
r = requests.head('http://httpbin.org/get')
print(r)
r = requests.options('http://httpbin.org/get')
print(r)

#######

#import requests
r = requests.get('https://api.github.com/events')
r.text
r.content
r.json()
#u'[{"repository":{"open_issues":0,"url":"https://github.com/...














