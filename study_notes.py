# ===============================================
# VARIABLES

# Variable = a box which stores data, has a name and value
number = 1
print(number)

# Variables are case sensitive and can't start with a number. The assignment operator in Py is the = sign

my_number = 1 + 2
print(my_number)
# The statement is evaluated then is printed

my_number = 1 + 2
my_second_number = 3 + 4
print(my_number + my_second_number)
# The result is 10

total = my_number + my_second_number
print(total)
# This makes it quicker

# ===============================================
# MATH

print(1 + 2)
# This gives back 3

print(type(0.5))
# This shows class 'float'

print(5 % 3)
# 3 goes into 5 with a remainder of 2, this is a modulo operation to find the remainder of a division

list = 1, 2, 3
print(sum(list))
# This returns 6

round(1.5)
# This rounds to the nearest whole no.

import math
from pickle import FALSE, TRUE
from re import L
from xml.dom.pulldom import SAX2DOM
math.floor(1.5)
# Rounds down to the nearest integer

math.ceil(1.5)
# Rounds up to the nearest integer

9 ** 2
# Exponential

# Whole numbers are integers, decimal numbers are floats

# ===============================================
# STRINGS

message = "I said "hello""
# This is a broken string - fix by using single quotes

message = 'I said "hello"'

# If you have a complex and long string, put triple speech marks on either end

# As standard, variables store numbers as strings

A + B
# This concatenates strings

"="*20
# This is useful for creating an underline:
====================

A = "part"
B = 1
A + B
# This won't work as a string and integer are not compatible

A + str(B)
# This will work as they are both strings now

"{1} {0}".format(A,B)
# This is a quicker method to print lines as strings. The numbers will print B then A

start = "I like "

middle = "to eat"

end = " pizza"

output = "{0} {1} {2}".format(start,middle,end)

print(output)


string.method()
# this is the formal for running a test on a string e.g.

"hello".count("e")
# this counts the number of the letter 'e's that appear in hello, which is 1

message = "Happy Birthday"
message.count("day")
#this works with functions, here 1 returns

message.upper()
> HAPPY BIRTHDAY

message.capitalize()
> Happy birthday

message.title()
> Happy Birthday

message.lower()
> happy birthday

message
> Happy Birthday

# The string didn't change as strings are unmutable, it can be overwritten though

message = message.upper()
message =
> HAPPY BIRTHDAY

message.islower()
> FALSE

message.isupper()
> TRUE

message.isalpha()
> FALSE
#Shows if everything is alphabetic. False as there is a space

message.isdigit()
> FALSE

message.isalnum()
> FALSE
# This shows whether alphanumeric

message.index("birthday")
> 6
# This shows the index number of where the element "birthday" starts, which is index number 6
# Index elements start from 0

message.index("hadsgiwd")
> -1
# This shows that the string does not exist
# Index is case sensitive
# Could be useful first converting the string to a particular case then running index

x = "000yes000"
x.strip("0")
> yes
# The 0's have been stripped

x.lstrip("0")
x.rstrip("0")
# These strip from the left or right side only

x.strip()
# This strips the spaces

len(x)
# Shows the length (num characters) of a string

name = input("what is your name?").strip
# If someone types "Jay  " it will strip the spaces

a = "sadboy"
a[0]
> h

a[start:end:step]
a[0:3:1]
> sad

# minus 1 from the start, go to the end

a[:3]
# This gives everything up to element 3

a[2:]
# This gives from the second element to the end

a[::-1]
# Goes from end to start reversing the string

a[-1]
# The very end value is -1
# This could be useful for getting say the 3rd to final element as it would be -3, rather than counting from the start

a(a.index("boy"))
> 3
# Shows which index "boy" starts from

a[a.index("sad"):a.index("boy")]
# The square brackets are important here

# Index only return the first time the slice is mentioned in the string


# ===============================================
# LOGIC
# Boolean is a data type which evaluates whether a statement is True or False
# 2 = 3     using the assignment operator - used for a function
# 2 == 3    using the equality operator - used to set/check if values are equal to eachother

# Logical comparison operators: ==, !=, >, <, <=, >=

2 == 3
> False
# This is evaluating if 2 is equal to 3

a = 100
b = 150

if a>b:
    print("a is bigger than b")
elif a<b:
    print("b is bigger than a")
else:
    print("a=b")

# Operators: combining if with not, and, or

not 4 == 3
> True (it is True that 4 does not == 3)

not 2 < 3
> False (it is False that 3 is not greater than 2)
# The not operator gives the opposite of the input, like a minus sign

C = 10
D = 5

if C > 10 and D > 1:
      print("it worked")
> Error (as both conditions were not satisfied)

if not (C > 10 and D > 1):
      print("it worked")
> "it worked" (false inside the brackets + false from not = true)


c = 5
d = -1

if c > 1 or d > 1:
    print("it worked")
> it worked

# not can be combined with the or to make it negative e.g.

if not (c > 1 or d > 1):
    print("it worked")
> Error

# false and true = false
# false or true = true
# it tries to be true but if both, it's false. If you're bad and good, you're still bad
# in general, not switches the sign of anything - work is out by thinking if a statement is overall positive or negative

#_____ Data Structures: Lists, Tuples, Dictionaries

our_list = [2, "A", 1, 7, TRUE]
print(our_list)
> [2, A, 1, 7, TRUE]
# Lists can have any type of variable

our_list[3]
> 7
# Selects the third element to bring it back

our_list[0:3:1]
> [2, "A", 1]

second_list = [4, 1, [5, 2], 7]
second_list[2][0]
> 5
# There is a list within a list. We queried the second element which is the second list, then then zeroth element within that list
# This follows the normal slicing rules

my_table = [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ]

my_table[0]
> [1, 2, 3]

my_table[1]
> [4, 5, 6]

my_table[2]
> [7, 8, 9]

# By doing this, we have rows and cols
# If we carried on with  lists within the above lists, we could make 3D structures, then 4D etc 
# Slices don't modify the list, they just take a copy

my_table[0][1]
> 2
# This is effectively like doing zeroth row, second col

l = [1, 2, 3]
2 in l
> TRUE

known_users = ["Jay", "Dan", "Eddie", "George", "Harry"]

print(len(known_users))
# Prints the length of the list i.e., num of known_users

# Deleting data:

example = [5, 2, 3, 2, 4]

example.remove("2")
print(example)
> [5, 3, 2, 4]
# removed the first occurance of "2"
# good when knowing the value to remove but leaves further occurances

del example[1]
print(example)
> [5, 3, 2, 4]
# removed element number one 
# good when knowing element num and ability to remove all occurances in one line by writing further elements

del example[0:2]
# can also cut out slices