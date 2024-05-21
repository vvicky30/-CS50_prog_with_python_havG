#let make cli-program to display meow (times of meow user enter) first by conventional method and then by argparser
 
'''
import sys

if len(sys.argv) == 1:  # in case where user doesn't enter anything after file name
    print("Meow")   # it simply prints one meow
elif len(sys.argv) == 3 and sys.argv[1]=="-n":
    n= int(sys.argv[2])  #first converting the user entered number (after-n) into integer
    print("\n Meow!" * n)  #then printing 'Meow!' n times 
else:   # if user entered anyhing else kinda default case 
    print("Usage of Meow_cli.py: please enter in this format(ex:) \n python Meow_cli.py -n 4")
    
   
o/p[on cosole]:
-python meow_cli.py
>Meow

-python meow_cli.py -n 6
>
 Meow!
 Meow!
 Meow!
 Meow!
 Meow!
 Meow!

-python meow_cli.py 5   
>Usage of Meow_cli.py: please enter in this format(ex:) 
 python Meow_cli.py -n 4
 
'''

'''

#now we;re going to use argparaser for making this cli program more systematic
import argparse  # we don't need sys to import argv

# going to call constructor of argparaser
parser = argparse.ArgumentParser()

parser.add_argument("-n")  #now going to add arguments or command line options with the help of add_argument -fn  

args = parser.parse_args() # now we're acessing parse.args fn with the help of object parser here 
                            # and saving its values to the args varibale
for _ in range(int(args.n)):
                               # rnage equals to value of n enterted by user while using -n as option; here we convert it first into int.
                        print("Meow!")       

o/p[on cosole]:
-python meow_cli.py -n 4
Meow!
Meow!
Meow!
Meow!

[if we enter numbers with unexpected option like we here does]:
-python meow_cli.py -b 4 
usage: meow_cli.py [-h] [-n N]    //it directs us to use help option which  -h to know what kinds of options available 
meow_cli.py: error: unrecognized arguments: -b 4   //error of unregnized arguments

[let's have a help option]:
-meow_cli.py -h  

>usage: meow_cli.py [-h] [-n N]   //it shows that we can use these option with it one is for help [-h] and another option is [-n N] here N denotes that it should be number after -n
options:
  -h, --help  show this help message and exit
  -n N       //as here nothing written to gives user a direction to use this option ....we can write description for specific option like help(above bydefault givng us description)  
'''


'''

import argparse

parser =argparse.ArgumentParser(description= "it will Moew like a CAT")   #here add description to argument parser 
parser.add_argument("-n",help="by choosing this option user can enter how many times to Meow!")  #here we add directions to use this argument 
arg = parser.parse_args()

for _ in range(int(arg.n)):
    print("Meow!")        

o/p[on cosole]:
-python meow_cli.py -h  
>usage: meow_cli.py [-h] [-n N]

it will Moew like a CAT     //now it's giving us the program description

options:
  -h, --help  show this help message and exit
  -n N        by choosing this option user can enter how many times  
              to Meow!
//and also it's giving us direction to use -n option here

[if we tries to run it like with unexprected arguments or not using any options like this ]:
-python meow_cli.py  //not using any option
 for _ in range(int(arg.n)):
                   ^^^^^^^^^^
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
// gives us error

[or if] :
-python meow_cli.py -n  
usage: meow_cli.py [-h] [-n N]
meow_cli.py: error: argument -n: expected one argument    //direct us to be enter one argument after using -n option (it  should be number as specifeid[-n N])
'''    
import argparse

parser =argparse.ArgumentParser(description= "it will Moew like a CAT")   #here add description to argument parser 
parser.add_argument("-n", default= 1, help="by choosing this option user can enter how many times to Meow!", type=int)  #here we add directions to use this argument 
                                #here i specified default value for option (-n) if user not specifically write any number after choosing this option
                                   # means by default it will print one 'Meow'
                                   # also specifed here that values user enter after choosing this option should be int type //so need to convert arg.n in to int during for-loop
arg = parser.parse_args()

for _ in range(arg.n):
    print("Meow!")    

'''
o/p[on cosole]:
-python meow_cli.py   
Meow!

[if user enter string instead of number after choosing -n option]:
python meow_cli.py -n fish
usage: meow_cli.py [-h] [-n N]
meow_cli.py: error: argument -n: invalid int value: 'fish'
//its throws error systematically that fish is invalid int ; which's true
'''