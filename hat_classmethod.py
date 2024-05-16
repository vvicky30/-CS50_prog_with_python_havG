# here we're going to illustrte the class method , by implementing method or function associated with class, 
# going to define method within class , and if we used decorator as : @classmethod over that function then that fn will be act as class-method.
#class method doesn't need object or instances of class to acess... class method directly can access through  class only as :
# Class_name.class_method_name()
import random

class Hat :
    # here we make instance method of intitializing attributes of instance/object
    #def __init__(self):
        #self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    # instead of making instance attributes , here we have to make class-attributes or class variables
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # like this     
    
    @classmethod
    def sort(cls, name):  # here we don;t need self(a it used for instances) here we used cls (as we're going to acess through class direcly)
        print(name, "is in", random.choice(cls.houses))
        # here we don't need self.name as here name variable will be acess through class not instances.
        

def main():
    Hat.sort("Harry")
# here sort function gives us random sort-hat corresponds to the "harry" as name we  pass as argument



if __name__=="__main__":
    main()    