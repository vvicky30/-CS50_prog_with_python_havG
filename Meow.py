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
# there's  