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
'''
  
# this time we're going to take int value from user
def meow(n:int)-> str:   # n should be the int , so we hinted it as of int class here like this 'n:int'
       # here we also specify one more type-hint that this fn should return value of str-type with the help of this operator : -> str (after function arguments) 
    for _ in range(n):
        print("Meow!")  # this function just printing meow as byproduct 
                           # not returning 'meow' of str clss/type 

number: int = int(input("what's number: "))  # and here we hinted number to be of int-class, meaning we  want number variable to be assign value of int-class only

m:str = meow(number)   # as function should ideally return 'meow' of str-type, this variable should be of type str only
print(m)  

#now we tried to run a above code with mypy :
mypy Meow.py
o/p>Meow.py:43: error: Missing return statement  [return]
Meow.py:49: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 2 errors in 1 file (checked 1 source file) 

//this it found two errors one at line 43 and other at 49 line 
// first error is saying missing return as fn doesn't retuning any value just forget about returning str-type value
// second error is that it's not assigning anything meaning 'None' to the variable m here
  
'''
# this times we resolve above type errors , this time fn will return hinted str type value 
# and m- variable will be assigned with str-type string 
def meow(n:int)-> str:   # n should be the int , so we hinted it as of int class here like this 'n:int'
       # here we also specify one more type-hint that this fn should return value of str-type with the help of this operator : -> str (after function arguments) 
    return "Meow! \n" * n  

number: int = int(input("what's number: "))  # and here we hinted number to be of int-class, meaning we  want number variable to be assign value of int-class only

m:str = meow(number)   # as function should ideally return 'meow' of str-type, this variable should be of type str only
print(m, end="")  
'''

#now we tried to run a above code with mypy :
mypy Meow.py
o/p> Success: no issues found in 1 source file    
// no isseues related to type-error found in this code now 
// as all variables and functions with hinted repective d-type satisfied while assigning values and retruning values

o/p on console :
what's number: 3
Meow!
Meow!
Meow!
'''