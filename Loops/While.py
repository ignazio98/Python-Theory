"""
we can execurte a set of istruction as long a condition is true
"""

i = 1
while i < 6:
    print(i)
    i += 1

#BREAK with this we can stop the loop even if the while condition is true:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#CONTINUE with this statement we can stop the current iteration and continue with the next
i = 1
while i < 6:
    i += 1    
    if i == 3:
        continue
    print(i)


i = 0
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")