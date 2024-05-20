# generally python is cosidered to be a type-script 
# as in python there's not a concept of defining or intializing a variable as a constant
#(all we can do is assigning constant value to the var in honoury terms) means developers should have sense that if variable with caps assigned constant value , just don't overwrite their values(as much as possible to aovid distortions in program)

# here's the simple program we made which takes user input and then spew 'meow' the times number entered by user.
'''
def meow(n):
    for _ in range(n):
        print("Meow!")

number = input("what's number: ")
meow(number)
 
[0/p]:
-what's number: 3
//as this will give me error that :  
TypeError: 'str' object cannot be interpreted as an integer
'''
# there's type-tester promineient in python with this 'mypy' type tester 
# we can test our codes whether our code have probably any type error or not (quite useful in complex code structure)
# firstly we have to install it through pip like this : pip install mypy
# once we install my py we will write our code in hinted method wherever we think it might generate type error like this :

'''


def meow(n:int):   # n should be the int , so we hinted it as of int class here like this 'n:int' 
    for _ in range(n):
        print("Meow!")

number: int = input("what's number: ")  # and here we hinsted number to be of int-class, meaning we  want number variable to be assign value of int-class only
meow(number)  

#now we tried to run a above code with mypy :
mypy Meow.py
o/p> Meow.py:30: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 1 error in 1 file (checked 1 source file)
// it shows a possible error at line number 30 where assignment takes place for variable 'number'
//and tell us expression to be assigned is of type str whereas variable has type int(as we hinted it with int-class)
  
'''
