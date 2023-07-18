# The try block lets you test a block of code for errors
# The except blocks lets you handle the error
# The else bloc klets you execute code when there's no error
# The finally block lets you execute code, regardless of the result of the try and except blocks


try:
    f = open('error-test.txt', 'w')
    f.write('Test write')
# This Input Output error will execute if there is no data or we try to read/write in the incorrect mode
except IOError: 
    print('ERROR: Could not find the file or data')
# This exception will execute if something other than a IO error happened
except:
    print('Something went wrong!')
# The else statement executes if there was no exceptions
else:
    print('File successfully edited')
    f.close()

# Now lets try to induce a IO Error by trying to write in the
# error-test.txt file when opened in read 'r' mode
try:
    test = open('IOError-test.txt', 'r')
    test.write('This is goint to throw an IOError, because we opened the file in "r" mode')
except:
    print('Something went wrong!!')
else:
    print('Success')
    test.close()
# The finally statement will execute no mater if it was an exception or not
finally:
    print('This block will execute no matter if it was an exception or not')

