
#showing how to use Parent and Child Classes i.e. the concept of Inheritance

# define the class
class Parent():
    
    # like a normal class the __init__ Constructor is defined as normal
    def __init__(self, last_name, eye_colour):
        print("Parent Constructor Called") # print when used
        # instance Variables        
        self.last_name = last_name
        self.eye_colour = eye_colour
    
    # Instance Method -> note: this is inherited by the Child and can be called or can be overwritten by creating a version in the child Class
    def show_info(self):
        print("last name:"+self.last_name)
        print("last name:"+self.eye_colour)
        
        
# define the class    
class Child(Parent):
    def __init__(self, last_name, eye_colour, number_of_toys):
        print("Child Constructor Called") # print when used
        # set Instance Variables can be defined by the Parent class (Inheritance)
        Parent.__init__(self, last_name, eye_colour)
        self.number_of_toys = number_of_toys
        
        
# An example of usage     
billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()