# as we know the round-fn that we used last while operating with float numbers is built-in fun
# but here in python we make our own trancate fn with 'def' defining fn approach
'''
in the truncation concept here we're going to replace 
the each digit with zero after given decimal point position
if decimal point position is 2 ; p=2
then in this ex: 234.56789
 o/p will be : 234.56000

this fn can be used for both negative and positive numbers
The truncation function can be implemented in the following way:
1. mutiplying the number(number that we're going to truncate) with 10 raied to pth power(where p is position after decimal values[in above ex: its 2]);10^p, to shift decimal point to the right.
2.then take interger part of above number-vlaue
3. and then devide that int value to 10^p to shift decimal point back to the left.   
'''
#defining the truncate fn 
#second arument reg. the decimal point positio 'p' by default will be zero
#if no second arg passed then i will return the int part of the number only as same happening in round-fn as well.
def truncate(n, dec_p=0):
    ten_raised_to_p = 10 **dec_p
    return(int(n*ten_raised_to_p)/ten_raised_to_p)

#here we make our another fn of currency formating of displying currency with periods 
def Currency(n):
    return(f"{n:,}")

print(truncate(3490122.487,2))
print(Currency(truncate(3490122.487,2)))
print(Currency(truncate(3490122.487,)))
print(Currency(truncate(-3490122.487,2)))
'''
3490122.48
3,490,122.48
3,490,122.0
-3,490,122.48
'''
    
# we can truncate digits towards the left of the decimal point
# by passing a negative number.
print(truncate(346.8, -1))
print(truncate(-26947.48, -3))
'''
340.0
-26000.0
'''
