# here we're going to make round-up and round-down fn using the
# the inbuilt fns from math liberary which're ceil and floor fn 
 
'''
Math.ceil(): This function returns the nearest integer that is greater than or equal to a given number. 
Math.floor(): This function returns the nearest integer less than or equal to a given number
'''
# here we're going to use the same approach as we're using in making our own truncation fn just with minor changes in 2nd-step
'''
1. mutiplying the number(number that we're going to truncate) with 10 raied to pth power(where p is position after decimal values);10^p, to shift decimal point to the right.
2.then take interger part of above number-vlaue
  2.a: for round_up fn we're going to take ceil-value of int.
  2.b: for round_down fn we're going to take floor-value of that int. 
3. and then devide that int value to 10^p to shift decimal point back to the left.   
'''
import math
# defining the round-up fn 
def round_up(n, decimal_p= 0):
    ten_raisedTo_p = 10 ** decimal_p
    return(math.ceil(n*ten_raisedTo_p)/ten_raisedTo_p)

# defining the round-down fn
def round_down(n, decimal_p=0):
    ten_raised_to_p = 10 ** decimal_p
    return(math.floor(n*ten_raised_to_p)/ten_raised_to_p)

print(round_up(12.567,))
print(round_down(12.467,))

print(round_up(12.567,2))
print(round_down(12.467,2))

print(round_up(3412.567,-2))
print(round_down(3512.467,-2))

print(round_up(-0.567))
print(round_down(-0.467))



'''
o/p:

13.0
12.0

12.57
12.46

3500.0
3500.0

0.0
-1.0
'''


#here again we're making round_half_up fn and round_half_down
'''
a) Rounding Half Up concept in Python:
The rounding half-up rounds every number to the nearest number with the specified precision and breaks ties by rounding up. 
The rounding half-up strategy is implemented by shifting the decimal point to the right by the desired number of places. In this case, we will have to determine whether the digit after the shifted decimal point is less than or greater than equal to 5. 
We can add 0.5 to the value which is shifted and then round it down with the math.floor() function.

b) Rounding Half Down concept in Python:
This rounds to the nearest number similar to the rounding half-up method, 
the difference is that it breaks ties by rounding to the lesser of the two numbers. 
Rounding half down strategy is implemented by replacing math.floor() in the round_half_up() function with math.ceil() 
and then by subtracting 0.5 instead of adding. 

'''
# defining round half up fn 
def round_half_up(n, decimal_p=0):
    ten_value_raised_to_p = 10 **decimal_p
    return(math.floor(n*ten_value_raised_to_p + 0.5)/ten_value_raised_to_p)

def round_half_down(n, decimal_p=0):
    ten_vlaue_raised_to_p = 10 ** decimal_p
    return(math.ceil(n*ten_vlaue_raised_to_p - 0.5)/ten_vlaue_raised_to_p)

print(round_half_up(12.567,)) #13.0
print(round_half_down(12.467,)) #12.0

print(round_half_up(12.567,2)) #12.57
print(round_half_down(12.467,2))#12.47

print(round_half_up(3412.567,-2))#3400.0
print(round_half_down(3512.467,-2))#3500.0

print(round_half_up(-0.567))#-1.0
print(round_half_down(-0.467))#0.0

'''
o/p:

13.0
12.0

12.57
12.47

3400.0
3500.0

-1.0
0.0
'''
