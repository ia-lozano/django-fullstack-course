# Some words before diving deep into decorators

# Storing a function into a variable
def greeting(name = 'PP'):
    return 'hello ' + name

print(greeting())

hello = greeting
print(hello())

# Functions can be called within another function
def func_1():
    print('Function func_1() started running')

    def func_2():
        print('func_2() started running too')

    def func_3():
        print('func_3 also started running')

    func_2()
    func_3()
    print('End of func_1()')

func_1()

# Returning functions into functions
def zero_detector(x = 0):
    print('zero_detector() started...')

    def is_zero():
        return 'x is equal to zero!'
    
    def not_zero():
        return 'x is NOT equal to zero!'
    
    if x == 0: return is_zero
    else: return not_zero

zdetector = zero_detector(1)
print(zdetector())

# Fucntions as arguments
def shout(string):
    return string.upper()

def whisper(string):
    return string.lower()

def modifier(function):
    string = function('This Text Is Going To Be Modified')
    print(string)

modifier(shout)
modifier(whisper)

# Manually creating a new decorator (a function that modifies the behavior of another function)
def new_decorator(function):
    
    def wrap_function():
        print('Code before executing the function')
        function()
        print('function() has been called')

    return wrap_function

def goes_inside_decorator():
    print('this needs to be inside the decorator')

goes_inside_decorator()

# goes_inside_decorator = new_decorator(goes_inside_decorator)
# goes_inside_decorator()
# The lines above can be replaced by:
@new_decorator
def this_also_goes_inside_decorator():
    print('Inside the decorator')

this_also_goes_inside_decorator()


