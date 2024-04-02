# here there's a concept in python 
# where we can pass our input through terminal while we're going to execute program in terminal.
# for that we use the sys liberary of python
import sys
# now we're going to print version of sys
'''
sys.version is used which returns a string containing the version of Python Interpreter 
with some additional information.This shows how the sys module interacts with the interpreter. 
'''
#print(sys.version)
'''
o/p:

3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
'''

'''
Input and Output using Python Sys:

The sys modules provide variables for better control over input or output. 
We can even redirect the input and output to other devices. 
This can be done using three variables --
  1. stdin (for standard input from terminal or console)
  2. stdout (for standard output to terminal or console)
  3. stderr (for throwing standard error to terminal or console)
  all these three looks similar to c/c++ module names becuse all we know that python interpreter developed through c++ lang,
  so eventually we can say python interpreter used GCC compiler behind the scenes after wrapping the high-level lang here
   
1. stdin: 
It can be used to get input from the command line directly. 
It is used for standard input. It internally calls the input() method. 
It, also, automatically adds ‘\n’ after each sentence.

'''
for inp_lines in sys.stdin:
    if 'quit' == inp_lines.rstrip():        
        #here rstrip: Return a copy of the string with trailing whitespace removed.
                                   #it basically check wether whatever user entered on terminal copy it and matches with our given word(here)"quit"  
         break  # going to break the control out of the loop when it encountered the keyword 'quit' on terminal entered by user
    print(f"You currently entering this: {inp_lines}")
# printing the meassage that you quitted when you entered the keyword 'quit' ; just for aesthetics
print("Here you quitted!") 

'''
o/p from console while user entering some inputs from there only and simultaneously console showing it:

python command_line_sys.py
hello how're you?
You currently entering this: hello how're you?

where're you?
You currently entering this: where're you?

are you going to quit now?
You currently entering this: are you going to quit now?

quit
Here you quitted!
'''
