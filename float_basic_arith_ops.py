#here first we're going to take values from user in float using float-fn same as we're doing for int
#here even if user doesn't enter decimal values ex:4 (instead of 4.0) it will automatically considered by fn to take it as 4.0 float no. instead of 4 as int.
x= float(input("enter the value of 'x': "))
y= float(input("enter the value of 'y': "))

print(x+y)

# as generally se in notes(currency)amounts of thausands and ten thausands with periods(",") before thusand & ten-thausand places {while sacnning from right to left , usual fasshion in numericals}
#Ex like 1,000 and 10,000 or 65,000 etc 
# for that we use string formatting approach here we can called it as float-formatting as here we're dealing with float numbers 
z = x+y
print(f"{z:,}") # as here we can see i am telling interpreter to read 'z' as speaical string where after print first digits it has to put period (,)
#here is the kinda of o/p i will give you 
'''
enter the value of 'x': 3445642.658
enter the value of 'y': 123456.654
3569099.312
3,569,099.312    (as here you can see we're printing float nos. in currency format with periods(,))

'''
#what if we want to round off the float to the nearest integer value ex: rounding-off (4.7) to 5.0 
'''
fn: round(number, ndigits)
    Parameter Values
    Parameter	Description
    here, number	: Required(not optional parameter) number to be rounded
    whereas, ndigits	: Optional-parameter. The numbers after decimals to use when rounding the number. Default is 0
'''
p = round(x+y,) # with deafualt zero as a optional parameter 
print(f"{p:,}")

'''
enter the value of 'x': 3456789.83456            
enter the value of 'y': 3556789.67894
7013579.513499999
7,013,579.513499999
7,013,580 (here you can see last digit was 79.51349999 now its rounded to nearest int which's 80 here )
'''
print(f"{round(x+y,2):,}") # here you can see in round-fn we're going to round off value to 2 digits after decimals 
'''
7,013,579.513499999 (this will)
7,013,579.51 (converted to this, as you can see here obly two value which's '51' here only viewed after decimal)
'''
# we can also used set precision rule functionality within formating as:-
b= x/y
print(b)
print(f"{b:3f}") # only print 6 numbers after decimal if we use'3f'
print(f"{b:.3f}") # only print 3 numbers after decimal if we use'.3f'
'''
0.9718848024745163
0.971885
0.972
'''
