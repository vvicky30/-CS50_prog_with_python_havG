# This program is for illustration of unit_testing in python 
# so what is unit-testing :- this type of testing generally done by various developers to test each and every specific part of overall source_code of module
# means in unit-testing developers usually test the speicic complex functions which's building blocks of or part of overall source_code or module .

# here we're going to illustrate the unit-testing where we're going to test square functions (basically two square function: one is correctly working and other is brocken-up due to the logical-error in its code) 
# this squre functions is part of this current python script(here: module) 

def main():
    number = int(input("enter some number to print its square"))
    squared_num1 = fine_square(number)
    squared_num2 = broken_square(number)
    print("this is your fine-squared number:",squared_num1)
    print("this is your broken-squared number:",squared_num2)
    
def fine_square(n):
    return n*n
    
    

def broken_square(n):
    return n+n   # here we made broken squre fn with logical erorr
                     # as instead of multiplying number to number itself , it's adding number to number itself.
                     # will definately gives error while testing for squaring-test-cases 
                     

if __name__ == "__main__":   # we're going to import these specific functions in another py-script for unit-testing purposes  
    main()                      # so we doesn't want to run this main function while importing these fns 

#we're going to unit-test these fns: fine_square & broken_square saperately 
#unit test through convenstional method which's not recommended it's quite manual and typically less compact [refer to test_conventional_sqr.py ]
#nit test through non-conventional method generally prefered by developers for unit-testing using funnctionalities of assertion 
# And further we build up on it more compact way of unit testing by using assertion functionality and pytest method [refer to file : testby_assertion_sqr.py and pytest_assertion_sqr.py]
    
    
'''
As expected both fns will work fine for number value is eual to 2: 
enter some number to print its square 2
this is your fine-squared number: 4
this is your broken-squared number: 4      {here as 2+2 'nd 2*2 both gives us 4 value }

As expected only fine_square-fn will work fine for number value is eual to 3:
enter some number to print its square 3
this is your fine-squared number: 9
this is your broken-squared number: 6
'''