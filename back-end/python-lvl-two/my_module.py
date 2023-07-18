def module_function():
    print("you're printing this from the my_module function")

def function():
    print('function() in my_module.py')

print('TOP lvl my_module.py')

if __name__ == '__main__':
    print('my_module.py is being run directly')
else:
    print('my_module.py has been imported')