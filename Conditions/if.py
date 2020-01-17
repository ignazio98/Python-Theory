"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""

#EXAMPLE:
x = 33
y = 10
if x > y:
    print('x is grater then y')
else:
    print('x is less than y')

#ELIF
a = 33
b = 33
if a > b:
    print("B is greater than a")
elif a == b:
    print("a equals b")

print("A") if a x > y else print("B")

c = 500
if a == b and b < c:        #or
    print("true")
