# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:09:37 2018

@author: hithr
"""

#From CS231n stanford
#http://cs231n.github.io/python-numpy-tutorial/
#%%
# the quicksort algorithm
def quicksort(arr):
    if len(arr) < 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
str_te = [5,1,32,5,65,6,34,4,63,46435,7634,6425,523523,]
print(quicksort(str_te))

#%%
#numbers
x = 3
x += 1
print(x)
x *= 2
print(x)
## this is to find the integer quotient from the divide
print(x // 3)
## this is to find the remainder of the divide
print(x % 5)
print(x ** 3)
y = 2.5343
print(type(y))

# boolean type
t = True
f = False

print(t and f)
print(t or f)
print(not f)
print(t != t)

# strings
# python has methods for strings
h = 'hello'
w = 'world'
print(h + " " + w)
print(len(h))
l = "love"
n = "qiwen yu"
ln = "guannan shen %s %s for %d days" % (l, n, 365*10000)
print(ln)
print(ln.title())
print(ln.capitalize())
print(ln.casefold())
print(ln.center(50))
print(ln.upper())
print(ln.replace('love', 'fuck'))

#%%
## the Containers
## list is the python equivalent of array
print("list can contain elements of different types")
xs = [3,1,2]
## the index start from 0
print(xs, xs[2])
## count from the end, from -1
print(xs[-2])
xs.append("bar")
xs[2] = "foo"
print(xs)
x = xs.pop()
print(x)
## access sublist:slicing
## range is a builtin function that create a list of integer
nums = list(range(5))
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2])
print(nums[:])
#slice can be negative, means delete from the end
print(nums[:-1])
#slice then assign new values
nums[2:4] = [8,9]
print(nums)
## numpy array also have slicing
# list is iterator, loop over the list
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# access the index with built-in function enumerate
for idx, animal in enumerate(animals):
    print("#%d: %s" % (idx + 1, animal))
# list comprehension with condition to simplify transform data
# with out list comprehension
nums[2:4] = [2,3]
print(nums)
squares = []
for x in nums:
    squares.append(x**2)
print(squares)

## with list comprehension
cubics = [x**3 for x in nums]
print(cubics)
## with condition if we like even
evensquares = [x**2 for x in nums if x % 2 == 0]
print(evensquares)

# Dictionaries, store (key, value) pairs, similar to a map in java
d = {'cat':'cute', 'dog':'furry'} #create a new dict

print(d['cat'])   ## print cute
print('cat' in d) # check if a dictionary has a given key, return boolean
d['fish'] = 'wet' # add an entry in the dict d
print(d['fish'])

# try keys with d.get
print(d.get('monkey', 'NA'))
print(d.get('fish', 'NA'))
del d['fish']
print(d.get('fish', 'NA'))

# iterate over keys in a dictionary
for animal in d:
    feature = d[animal]
    print('When you see %s, %s will come into your mind' % (animal, feature))

## easily construct dictionary from list, dict comprehension
even_num_square = {x:x**2 for x in nums if x % 2 == 0}
print(even_num_square)

# set
# set is unordered collection of distinct elements
new_animals = {'cat', 'dog'}
## use print to check, boolean
# in command in set, the idea from the math

print('cat' in new_animals)
print('chicken' in new_animals)

# the method for set
new_animals.add('fish')
print('fish' in new_animals)
print(new_animals)
print(len(new_animals))
new_animals.add('fish')
print(len(new_animals))
new_animals.remove('fish')
print(len(new_animals))

## loop over set has the same syntax with loop over list
