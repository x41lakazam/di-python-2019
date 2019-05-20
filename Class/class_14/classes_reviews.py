##### CLASS REVIEWS #####

# Definition of a class

# In the class definition, you can add a parent class

# __init__ method is the function that is called on the object creation

# Every class method should receive self as argument, this represents the
# object itself

# Example: 

#class NameOfTheClass(ParentClass):
#
#    def __init__(self, argument1, argument2, default=defaultvalue):
#        self.value1         = argument1
#        self.value2         = argument2
#        self.default_value  = defaultvalue

class Fish():

    def __init__(self, color, name):

        self.color = color
        self.name  = name

        self.living_habitat = "water"

    def talk(self):
        print("{} says: ...".format(self.name))

    def describe(self):
        print("The {} is {}".format(self.name, self.color))

my_fish = Fish("green", "greenfish")
#my_fish.talk()
#my_fish.describe()

class Salmon(Fish):

    def describe(self):
        print("The {} salmon is {}".format(self.name, self.color))

royal_salmon = Salmon(name="Royal", color="white")
#royal_salmon.describe()

class Student:

    def __init__(self, name, mail, age):
        self.name = name
        self.mail = mail
        self.age  = age

        self.marks = []

    def __repr__(self):
        return "Student {}: {} years old (contact: {})".format(self.name,
                                                              self.age,
                                                              self.mail)

reuven = Student("Reuven Tal", "ruvi@gmail.com", 28)
#print(reuven)

class Class:

    def __init__(self, classname):
        self.classname = classname
        self.students  = []


    def add_student(self, student_obj):
        self.students.append(student_obj)

    def describe(self):
        print("Class {}".format(self.classname))
        print("Students:")
        for student in self.students:
            print(student)



pythonclass = Class("Python Web 2019")
student1    = Student("Mickey Mouse", "mickey@mouse.com", 100)
student2    = Student("Mike", "mike@gmail.com", 23)
pythonclass.add_student(student1)
pythonclass.add_student(student2)
pythonclass.add_student(reuven)
pythonclass.describe()
