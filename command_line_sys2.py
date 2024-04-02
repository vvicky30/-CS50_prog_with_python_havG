'''
stdout: 
A built-in file object that is analogous to the interpreter’s standard output stream in Python. 
stdout is used to display output directly to the screen console. Output can be of any form, 
it can be output from a print statement, an expression statement, and even a prompt direct for input. 
By default, streams are in text mode. In fact, wherever a print function is called within the code, 
it is first written to sys.stdout and then finally on to the screen. 
'''
import sys
# here we going to write on terminal using stdout object of sys liberary(class here) ,
# specifically here we use write function of sys.stdout
sys.stdout.write("Hello this mesaage is written through sys.stdout")

#o/p: Hello this mesaage is written through sys.stdout

'''
stderr: 
Whenever an exception occurs in Python it is written to sys.stderr. 

This code will print the string “Hello World” to the standard error stream. 
The sys.stderr object represents the standard error stream, 
and the print() function writes the specified strings to the stream.
'''
def writingmy_err(*a):  # here * asterisk used for allowing user to pass variable number of arguments to fn here.
    print(*a, file = sys.stderr) # writing here the argument(here that argument is string;sentence) as error to error stream file which's sys.stderr
   
writingmy_err("MyError: so this is how i write my own error")  # this will definitely showed up on console first as its error
sys.stderr.write("write my error here shortly")   # another way to write on that error stream file 

'''
o/p on console:
MyError: so this is how i write my own error
write my error here shortlyHello this mesaage is written through sys.stdout
'''