#A sets is a collection which is unordered and unindexed.
thisets = {'apple', 'banana', 'cherry'}
print(thisets)

"""
ACCESS ITEMS
"""
#we can loop through the set items using a for loop
for x in thisets:
    print(x)        

#print banana if it's in the sets
print('banana' in thisets) 

"""
CHANGE ITEMS
"""
#once a ste is created, you can't change its element, but you can add new element
thisets.add('orange')
print(thisets)

#or adding multiple items with update()
thisets.update(['mango', 'grapes'])

"""
REMOVE ITEMS   
"""
thisets.remove('banana')
print(thisets)

#you can use different way to delete an item or items from a sets, for example
#pop(), discard() or clear() (last function is used to deprive all the items in the set)
#or del nameset for delete the set

"""
JOIN TWO SETS
"""
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#or you can use the function update(), both will exclude any duplicate items

#add()	                        Adds an element to the set
#clear()	                    Removes all the elements from the set
#copy()	                        Returns a copy of the set
#difference()	                Returns a set containing the difference between two or more sets
#difference_update()	        Removes the items in this set that are also included in another, specified set
#discard()	                    Remove the specified item
#intersection()	                Returns a set, that is the intersection of two other sets
#intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	                Returns whether two sets have a intersection or not
#issubset()	                    Returns whether another set contains this set or not
#issuperset()	                Returns whether this set contains another set or not
#pop()	                        Removes an element from the set
#remove()	                    Removes the specified element
#symmetric_difference()	        Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	Inserts the symmetric differences from this set and another
#union()	                    Return a set containing the union of sets
#update()	                    Update the set with the union of this set and others