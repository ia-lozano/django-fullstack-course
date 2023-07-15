# Use the "class" keyword to create your own objects
# class name is capitalized by convention
class Sample():
    pass

x = Sample()
print(type(x))

# An example of a Dog() object for attributes

class Dog():
    # CLASS OBJECT ATTRIBUTE (will be constant for every instance of Dog())
    species = 'mammal'
    # Special method (__method__) for initialization
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog('chihuahua', 'Tina')
print(mydog.name, mydog.breed, mydog.species)

# Object methods: The object Circle() has a class object attribute equal
# to pi, an attribute wich is its radius, and two methods, 
# one for calculating the area and other that re-assigns the radious
class Circle():
    pi = 3.14

    def __init__(self, r):
        self.radius = r

    def area(self):
        # with self.r we indicate the method to search in the object attributes
        # and with Circle.pi, the method searches through the class object attirbutes
        return self.radius*self.radius*Circle.pi
    
    def set_radius(self, new_r):
        self.radius = new_r

big_circle = Circle(5)
print(big_circle.area) # This will print info about the method
print(big_circle.area()) # This will print the actual area result
print(big_circle.set_radius(1)) # This prints None because set_radius method doesn't return anything
print(big_circle.area()) # New area with r = 1

#INHERITANCE
class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def whoAmI(self):
        print('ANIMAL')

    def eat(self):
        print('EATING')

animal = Animal()
animal.whoAmI()
animal.eat()

# The new class Cat() will inherit some Animal() methods
# Pass the class to be inherited as an argument
class Cat(Animal):

    def __init__(self):
        # Anima.__init__(self):
        print('CAT CREATED')

    def meow(self):
        print('MEOW')

    # It's possible to override inherited methods
    def eat(self):
        print('CAT EATING')

cat = Cat()
cat.whoAmI()
cat.meow()
cat.eat()


# SPECIAL METHODS

# __str__() special method shows the string representation of your object
# when you use a function that searches for this method (like print()), it will search
# through the string representation of your object.

class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title: {}, Author: {}, Pages: {}'.format(self.title, self.author, self.pages)
    
    # len() returns anything you write in the function, in this case
    # the length of the book is its pages number
    def __len__(self):
        return self.pages
    
    # del method, literally deletes the object
    def __del__(self):
        print('a book is destroyed!!')

book = Book('Python', 'For Dummies', 90)
print(book)    
print(len(book))
del book
# print(book) # This will return a NameError because the book object was deleted