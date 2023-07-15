# Scopes for variables LEGB
'''
L: Local - Names assigned within a function (def or lambda), and not declared global in that function
E: EFLs - Name in the local scope of any and all enclosing functions
G: Global - Names assigned at the top level of a module or file, or declared global in a def within the file
B: Built-in - Names preassigned in the built-in names module: open, range, SyntaxError,...
'''

# Global X
x = 25

def funcx():
    # Local X in func()
    x = 50
    return x

print('Global X = ', x)
print('Local X = ', funcx())

# Even if we call func() first, the value of global X is still the same
funcx()
print('Global X again = ', x)

# Passing global X as an argument, and then reassigning it
def funx_v2(x):
    # At first, the function takes the global value
    print('X is: ', x)
    # Then reassigns it
    x = 1000
    print('local X reassigned to ', x)

funx_v2(x)
print('Global X: ', x)

# Global keyword (try to avoid it whenever possible)
def func_global():
    global x
    x = 1000

print('Before function call X is: ', x, ' (global X)')
func_global()
print('After function call X is: ',  x, ' (global X changed its value due to global declaration inside the funcion)')

# X local to lambda
lambda x: x**2

# Enclosing function locals
name = 'Global name'

def greet():
    # If we delete this local assignment of the "name variable", hello() will take the global variable
    name = 'Enclosed name'

    def hello():   
        print('hello ' + name)
    # hello() must be called in order to print the result, greet() only reassigns the variable
    hello()

greet()
print(name)

# Built-in Level
# They're reserved words, don't even try to reassign them (len, True, False, def, ...)
