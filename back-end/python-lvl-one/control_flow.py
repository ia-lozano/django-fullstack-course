# => COMPARISON AND LOGICAL OPERATORS

# Greater than
5 > 3
# Less than
3 < 5
# Greater than or equal to
1 >= 1
# Less than or equal to
1 <= 1
# Equality (checks for data type and value)
5 == 5
# Inequality
1 != 0

# => LOGICAL OPERATORS

# They're literally "and" and "or"
(2 > 3) and (4 < 8)
(1 == 2) or (7 < 10)

# => IF STATEMENT (note the identation to make code blocks)

if 1 < 2:
    print('Yes')
elif 1 == 0:
    print('Maybe')
else:
    print('No')

# => LOOPS

# The For Loop: It is possible to iterate through any indexable data type or structure
# Iterating through a list
lst = [1, 2, 3, 4, 5, 6]
for i in lst:
    print(i, end = ' ')
print('\n')

for j in range(10):
    print(j, end = ' ')
print('\n')

# Iterating through a dictionary
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for k in dic:
    print(k, end = ' ')
print('\n')
for v in dic:
    print(dic[v], end = ' ')
print('\n')

# Iterating through a tuple
pairs = [(2, 4), (6, 8), (10, 12)]
for tup in pairs:
    print(tup, end = ' ')
print('\n')
# Unpacking the tuples
for (tup1, tup2) in pairs:
    print(tup1, end = ' ')
    print(tup2, end = ' ')

# The While Loop
i = 0
while i < 5:
    print('i is: {}'.format(i))
    i += 1

# => LIST COMPREHENSION

x = [1, 2, 3, 4, 5]
# NOT using List Comprehension
output = []
for i in x:
    output.append(i**2)
print(output)
# USING List Comprehension
y = [j**2 for j in x]
print(y)

# "Filtering" a list (not using the filter function)
lst = [10, 15, 20, 25, 30, 35, 40, 45, 50]
lst_evens = [i for i in lst if i%2 == 0]
print(lst_evens)