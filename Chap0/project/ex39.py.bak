# -*- coding: utf-8 -*-

## ex 39 字典

# BE 00

#create a mapping of state to abbreviatuion

from collections import OrderedDict

states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New Youk':'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some citys
print '-' * 10
print "NY state has:",cities['NY']
print "OR state has:",cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ",states['Michigan']
print "Florida's abbreviation is: ",states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ",cities[states['Michigan']]
print "Florida has: ",cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state,abbrev in states.items():
    print "%s is abbreviated %s" % (state,abbrev)

# print every city in state
print '_' * 10
for abbrev,city in cities.items():
    print"%s has the city %s" % (abbrev,city)

# now do both at the same time
print '+' * 10
for state,abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state,abbrev,cities[abbrev])

print '_' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas',None)

if not state:
    print "Sorry,no Texas."

# get a city with a default value
city = cities.get('TX',"Does Not Exist")
print "The city for the state 'TX' is ; %s " % city

# test
print '\\\\' * 10
D = {
    1:'一',
    2:'二',
    3:'三',
    4:'四',
}
print D.values()
print D.keys()
print D.viewitems()


for value in D:
    print D.get(value)

od = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
print od['a']
print od


# DK

# 01 字典的更多操作

     # |  clear(...)
     # |      D.clear() -> None.  Remove all items from D.
     # |
     # |  copy(...)
     # |      D.copy() -> a shallow copy of D
     # |
     # |  fromkeys(...)
     # |      dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
     # |      v defaults to None.
     # |
     # |  get(...)
     # |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     # |
     # |  has_key(...)
     # |      D.has_key(k) -> True if D has a key k, else False
     # |
     # |  items(...)
     # |      D.items() -> list of D's (key, value) pairs, as 2-tuples
     # |
     # |  iteritems(...)
     # |      D.iteritems() -> an iterator over the (key, value) items of D
     # |
     # |  iterkeys(...)
     # |      D.iterkeys() -> an iterator over the keys of D
     # |
     # |  itervalues(...)
     # |      D.itervalues() -> an iterator over the values of D
     # |
     # |  keys(...)
     # |      D.keys() -> list of D's keys
     # |
     # |  pop(...)
     # |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     # |      If key is not found, d is returned if given, otherwise KeyError is raised
     # |
     # |  popitem(...)
     # |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
     # |      2-tuple; but raise KeyError if D is empty.
     # |
     # |  setdefault(...)
     # |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     # |
     # |  update(...)
     # |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
     # |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     # |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     # |      In either case, this is followed by: for k in F: D[k] = F[k]
     # |
     # |  values(...)
     # |      D.values() -> list of D's values
     # |
     # |  viewitems(...)
     # |      D.viewitems() -> a set-like object providing a view on D's items
     # |
     # |  viewkeys(...)
     # |      D.viewkeys() -> a set-like object providing a view on D's keys
     # |
     # |  viewvalues(...)
     # |      D.viewvalues() -> an object providing a view on D's values
     # |
