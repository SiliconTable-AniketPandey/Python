# If you remove the commented code in fifth line the code will not work
class Person():
    def __init__(self, name, age):
        self.name = name
        #self.__age = age        # Will not work as we are declearing age as a private variable by using double underscore '__' 
        self.age = age                        # before the variable so the child class won't be able to access the variable
                                # Will produce AttributeError: 'Person' object has no attribute 'age'
    def display(self):
        print(self.name,self.age)   
