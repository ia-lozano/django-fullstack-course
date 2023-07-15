# FUNCTIONS
def func1(param = 'default'):
    '''
    THIS IS THE DOC STRING
    func1(param) returns a string.format() with the parameter
    '''
    print('The entered parameter was: {}'.format(param))

func1()
func1(40)
func1(True)
func1('generic string')

def Hello_world(word):
    if word == 'print':
        print('Hello world')
    else: print('')

Hello_world('print')
Hello_world('other arg')

# The  return statement
def integer_add(x, y, z=0):
    '''
    This function only adds integer numbers
    '''
    if type(x) == type(y) == type(0):
        return x + y + z
    else: return '3RR0r: Arguments must be integers!'

print(integer_add(5, 3))
print(integer_add('a', 1))
print(integer_add(1, 2, 4))

# LAMBDA EXPRESSIONS
# A lambda expression is an anonymous function that take multiple arguments but just one expression
# Its basic structure is => lambda arguments: expression

func = lambda x, y, z = 0: x + y + z
print(func(1, 2))
print(func(1, 2, 5))

# => The filter function
nums = list(range(11))
# This is what the filter function looks like in a traditional function
def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, nums)
print(list(evens))

# This is what the filter function looks like into a lambda expression
evens_lambda = filter(lambda num: num%2 == 0, nums)
print(list(evens_lambda))

# => The map function
# This is what the map function looks like in a traditional function
def double_num(num):
    return num + num

doubles = map(double_num, nums)
print(list(doubles))

# This is what the map function looks like in a lambda function
doubles_lambda = (map(lambda num: num+num, nums))
print(list(doubles_lambda))