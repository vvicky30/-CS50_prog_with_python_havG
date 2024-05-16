

#As we know in the OOP_student.ipynb file this was last version of code we have in the file :
'''
class Student:
    def __init__(self, name , house):
        self.name = name             # setter version will be called here
        self.house = house          # this is also going to call setter version of house
    
    def __str__(self):  # for string representation of object 
        return f"{self.name} from {self.house}" 
    
    
    @property         # getter version
    def house(self):
        return self._house     # this version of function simply return whtever valid house(attribute values)value entered by user
                              # _house is converted to private attribute , and in this way its also avoiding collision with function name here.
    
    @house.setter    # setter version
    def house(self, house):
        #here we can include that validity code for house names 
        # house name is valid then allowed to set it up as that assigned name.
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin","Seventh-House"]:
            raise ValueError("Invalid-House!!...please enter valid house")
  
        self._house = house   # here we make our house attribute a private attribute with the help of "_"
    
    @property    # getter version
    def name(self):
        return self._name
    
    @name.setter    # setter version
    def name(self, name):
        if not name:   # checking that name can't be blank
               # here we raise our own error , this will be raised actually when constructor calling and object creation take place
            raise ValueError("Missing name!!...please enter name")
        self._name= name
        
        
def main_correctness():   
    student= get_student()    
    # here we going to print object named student simply: 
    print(student)
def get_student():
    n= input("Student_name:").strip().title()
    h= input("Student_house:").strip().title()

    #student = Student(n,h)
    return Student(n,h)  # directly returning 
if __name__=="__main__":
    main_correctness() 
'''
#here we can see the function get_student is function outside the class_Student and using class instance to assign values of name and house 
# function associated with class is not recommanded by developers to define outside the class as all the components of the class should be encapsulated in the class itself.
#so here we have to make class-method named get-fn which assigns those vlaues from user to the attributes of the classes.

class Student:
    def __init__(self, name , house):
        self.name = name             # setter version will be called here
        self.house = house          # this is also going to call setter version of house
    
    def __str__(self):  # for string representation of object 
        return f"{self.name} from {self.house}" 
    
    
    @property         # getter version
    def house(self):
        return self._house     # this version of function simply return whtever valid house(attribute values)value entered by user
                              # _house is converted to private attribute , and in this way its also avoiding collision with function name here.
    
    @house.setter    # setter version
    def house(self, house):
        #here we can include that validity code for house names 
        # house name is valid then allowed to set it up as that assigned name.
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin","Seventh-House"]:
            raise ValueError("Invalid-House!!...please enter valid house")
  
        self._house = house   # here we make our house attribute a private attribute with the help of "_"
    
    @property    # getter version
    def name(self):
        return self._name
    
    @name.setter    # setter version
    def name(self, name):
        if not name:   # checking that name can't be blank
               # here we raise our own error , this will be raised actually when constructor calling and object creation take place
            raise ValueError("Missing name!!...please enter name")
        self._name= name

    @classmethod
    def get(cls):
        n= input("Student_name:").strip().title()
        h= input("Student_house:").strip().title()  
        return cls(n,h)


def main_correctness():   
    student= Student.get()   # going to access get method which's class-method through class only.
    print(student)

'''
[on console]:-

Student_name:   harry  
Student_house:  gryffindor
Harry from Gryffindor
'''



if __name__=="__main__":
    main_correctness() 
