#A tuple is a collection which is ordered and unchangeable.
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

"""
ACCESS TUPLE ITEMS
"""
#positive position
print(thistuple(1))

#negative position
print(thistuple(-1))

#range position
secondtuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(secondtuple[2:5])

print(secondtuple[-4:-1])


"""
CHANGE TUPLE VALUES
"""

#there is one only way to change a tuple, you should convert it into a list,
#change the element, that you desire, and convert again into a tuple

x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)

print(x)

"""
LOOP WITH TUPLE
"""

for x in thistuple:
    print(x)            #print element one to one

if 'apple' in thistuple:
    print('YESSSS')

"""
TUPLE FUNCTIONS
"""

#Length
print(len(thistuple))

#One type
tuple3 = ('apple',)
print(type(tuple3))

#Count every time the value appears in the tuple
thistuple.count('apple')

#Index, return the first position of the value in the tuple
ris = thistuple.index('banana')