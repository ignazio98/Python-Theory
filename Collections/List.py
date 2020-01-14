#documentation about the list of string and numbers

#print all list element
thislist = ['apple', 'banana', 'cherry']
print(thislist)

#-----------------------------

#access items at the element in position 1
print(thislist[1]) 

#------------------------------

#access items with negative index
print(thislist[-1])

"""
RANGE OF INDEX
"""
#print(from the second included to the fifth excluded)
secondlist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(secondlist[2:5])

#---------------------------

#from the beginning to the fourth position
print(secondlist[:4])

#---------------------------

#from the second to the end of the list
print(secondlist[2:])

#---------------------------

#print the last 4 element
print(secondlist[-4:-1])


"""
CHANGE ITEM VALUE
"""
thislist[1] = 'blackcurrent'
print(thislist)

"""
LOOP THROUGH A LIST 
"""
for x in thislist:
    print(x)        #print all the element of the list, one by one

#-----------------------------

if 'apple' in thislist:
    print('Yes, apple is in the fruits list')

"""
LIST FUNCTION
"""
print(len(thislist))       #list length

#add element form list
thislist.append('orange')
thislist.insert(1, 'banana')
print(thislist)        

#---------------------------------

#delete element form list
thislist.remove('banana')
thislist.pop()              #delete the last element of the list
del thislist[0]             #delete the element in the first position
thislist.clear()            #empties the list
print(thislist)            

"""
COPY THE LIST
"""
mylist = thislist.copy()
print(mylist)

#--------------------------

list2 = list(thislist)
print(list2)

"""
JOIN TWO LISTS
"""

listone = ['a', 'b', 'c']
listwo = [1, 2, 3]              

listhree = listone + listwo     #concatenate the second list to the first list
print(listhree)

#------------------------
for x in listwo:
    listone.append(x)           #append the second list to the first list

print(listone)
#------------------------

#listone.extend(listwo)


"""
LIST() COSTRUCTUR
"""
#define the list structor
thislist2 = list(('apple', 'banana', 'cherry'))
print(thislist2)


#END