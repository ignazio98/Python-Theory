#A dictionary is a collection which is unordered, changeble and indexed
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict)

"""
ACCESSING ITEMS
"""
#you can access the items with the key name
x = thisdict['model']
y = thisdict.get('brand')
print(x)
print(y)

"""
CHANGE VALUES
"""
thisdict['year'] = 2018

#Print all key names in the dictionary, one by one
for x in thisdict:
    print(x)

#Print all values in the dictionary
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

#Print keys and values, with items() function
for x,y in thisdict.items():
    print(x, y)

"""
CHECK IF EXISTS
"""
if 'model' in thisdict:
    print('YES, is one of the keys')

"""
DICTIONARIES OPERATION
"""

#ADDING:
thisdict['color'] = 'red'
print(thisdict)

#REMOVING: 
#popitem(remove the last inserted item)
thisdict.pop('color')
print(thisdict)

#COPY
#or dict() method
mydict = thisdict.copy()
print(mydict)

"""
NASTED DICTIONARIES
"""
myfamily = {
    'child1' = {
        'name': 'Emily'
        'year': 2004
    },
    
    'child2' = {
        'name': 'Tobias'
        'year': 2007
    },
    
    'child3' = {
        'name': 'Linus'
        'year': 2011
    }
}