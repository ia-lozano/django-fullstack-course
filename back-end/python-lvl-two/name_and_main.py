# For this we're going to recycle the my_module.py file
import my_module
print('TOP lvl name_and_main.py')
my_module.function()

if __name__ == '__main__':
    print('name_and_main.py is being run directly')
else:
    print('name_and_main.py has been imported')