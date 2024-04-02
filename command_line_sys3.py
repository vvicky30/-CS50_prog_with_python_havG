'''
Command Line Arguments  [sys.argv] here argv tands for argumrnt-vector
Command-line arguments are those which are passed during the calling of the program along with the calling statement. 
To achieve this using the sys module, the sys module provides a variable called sys.argv. It’s main purpose are:

It is a list of command-line arguments.
len(sys.argv) provides the number of command-line arguments.
sys.argv[0] is where it stores the name of the current Python script.
sys.argv[1 to n] stores whatever user pass through commandline while executing python-script

Example: Consider a program for adding numbers and 
the numbers are passed along with the calling statement.

This code calculates the sum of the command-line arguments passed to the Python script. 
It imports the sys module to access the command-line arguments and then iterates over the arguments, converting each one to an integer 
and adding it to a running total. Finally,it prints the total sum of the arguments.
'''
import sys 
print(f"so here is the total numbers you entered: {len(sys.argv)-1} \nhere are those number you entered: {sys.argv[1:]}")
                                              # here after taking length of argv we minus it with 1 'coz it also going to count python-file name 
                                              # which is bydefault stored at argv[0]

print("here we're iterating over your entered C-L-arguments/values:-")
for num in sys.argv[1:] :
    # here we're running the for loop in argv which stores multiple command line-arguments in list 
                               # here we deliberately skip zero index as on argv[0] it stores python-script name (or this program file name)
                               # here we used the methodology of subsetting [as: argv[1:]] means it acess from argv[1] to long on as much as possible , 
                                  # depends on user that how much he/she entered values in command lines
    print(num)                              

# now for calculating total sum of the C-l values entered by user
# first we have to make variable for length , to which for loop end
n= len(sys.argv)
sum = 0
for i in range(1,n):
    print(f"here is your {i}-ELE: {sys.argv[i]}")
    sum += int(sys.argv[i]) # here we have to convert each elemet of argv from string to int

print(f"total sum of the C-L-values is: {sum}")  

'''
on console (o/p):-

command_line_sys3.py 1 8 6 7 3 9
so here is the total numbers you entered: 6 
here are those number you entered: ['1', '8', '6', '7', '3', '9']
here we're iterating over your entered C-L-arguments/values:-
1
8
6
7
3
9
here is your 1-ELE: 1
here is your 2-ELE: 8
here is your 3-ELE: 6
here is your 4-ELE: 7
here is your 5-ELE: 3
here is your 6-ELE: 9
total sum of the C-L-values is: 34
''' 

     
