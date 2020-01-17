"""
FOR LOOPS
is used for iterating over a sequence (list string dictionary ecc)
it works like a n iterator method as found in other object-oriented programming languages
"""

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        break                   #continue statement
    else:
        print(x)
else:
    print("For loop is end")

#LOOP A STRING
for y in "banana":
    print(y)

#RANGE 
#function returns a sequence of numbers, starting from 0 by default, and increaments by 1 and ends at a specific number
for x in range(6):
    print(x)

#range(2, 30, 3) start from 2 finish at 30 and increment the sequence 3 and not 1

#NESTED FOR

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)