# => NUMBERS: float (with a decimal position), or integers
gross_income = 100 # Integer
tax_rate = 0.1 # Float
tax_payment = gross_income*tax_rate
net_income = gross_income - tax_payment
print('Total Income: ', gross_income, '\nTax to Pay:   ', tax_payment, '\nNet Income:   ', net_income)

# => STRINGS: Immutable and indexable
hello = 'Hello'
# INDEXING
print(hello[0], hello[-1])
# SLICING
longstr = 'vervoerdersaansprakelijkheidsverzekering'
# Grab all elements from the 2nd index to the end of the string:
print(longstr[2: ])
# Grab everything from the beginning to the 6th index (not included):
print(longstr[:6])
# Grab everythin from the 2nd index (included) to the 20th index (not included):
print(longstr[2:20])
# Grab every index but in steps of two
print(longstr[::2])
# METHODS
word = 'anti constitucionalmente'
# Turn strings to lower case and upper case, or capitalize them
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.split(' ')) # returns a list with the splitted string elements
# PRINT FORMATS
fstring = 'Item One: {} Item Two: {}'. format('dog', 'cat')
print(fstring)
# Formating by item assignment:
fstring2 = 'Item A: {a}, Item B:{b}'.format(b = 'Second', a = 'Fist')
print(fstring2)

# => LISTS: Indexable and mutable (similar to JavaScript arrays)
mylist = ['a', 'b', 'c', 'd', 'f']
print('original list: \n', mylist)
mylist[2] = 'reassigned'
print('reasigned list: \n', mylist)
# METHODS
# Appending an item at the end of the list
lstA = [1, 2, 3, 4, 5]
lstA.append(85)
print(lstA)
# Use .extend() to add multiple elements 
lstA.extend(['a', 'b', 'c'])
print(lstA)
# Remove the last item with .pop() method
lstA.pop()
print(lstA)
# Put an index to the pop() method to specify the 
deleted = lstA.pop(1)
print(deleted)
print(lstA)

#Altering the order of the list elements
lstA.reverse()
print('lstA reversed: ', lstA)
lstB = [5, 8, 90, 41, 22, 1, 0]
# Sorting elements
# Note that the sort() method does not return a value, it changes the original list
# and can only be used with numbers...
lstB = [91, 45, 88, 0, 4, 1]
lstB.sort()
print('lstB.sort() => ', lstB)
# In the other hand, sorted() method returns a value that can be stored in a variable
# Note that sorted() only works with lists, also, sorted is a function
lstC = [77, 32, 1, 89, 0, 45]
lstD = sorted(lstC)
print('Original lstC: ', lstC ,'\nsorted(lstC) stored in lstD: ', lstD)

# Nested lists
nested_list = [1, 2, ['x', 'y', 'z', '0']]
# For nested lists, we can get any element using doble square bracket [][]
print(nested_list[2][1])
# Create a matrix by nesting lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0])
# A brief word about LIST COMPREHENSION
first_col = [row[0] for row in matrix]
print(first_col)

# => DICTIONARIES: They do not retain any order, they use a key:value system
dict1 = {'k1': 'v1', 'k2': 'v2', 'k3':{'knested':[1, 2, 'grabMe']}}
# Grab the 'grabMe' string into the dictionary
print(dict1['k3']['knested'][2])
# It is possible to apply a method to the grabbed item
print(dict1['k3']['knested'][2].upper())
# Mutating dictionaries
food = {'breakfast': 'tacos', 'lunch': 'sushi','dinner': 'pizza'}
print('Original food Dictionary: ', food)
# adding a new key, value pair:
food['trap lunch'] = 'chips'
# modifying a value:
food['breakfast'] = 'cigarette & redbull'
print('Modified food Dictionary: ', food)

# BOOLEANS: true or false, you know: True and False
print(False or True)
print(True and False)
print(False and False)
print(True and True)

# => TUPLES: Indexable but ummutable
tuple1 = (1, 2, 3)
print(tuple1[0] + tuple1[2]) # Indexing the tupple

# => SETS: Not indexable, unordered collection of unique elements
set1 = {1, 2}
print('Original Set: ', set1)
# Adding elements to the set with the .add() method
for i in range(4):
    set1.add(i)
# Note that the for loop only added 0 and 3, because 1 and 2 were already in the set
print('New Set: ', set1)