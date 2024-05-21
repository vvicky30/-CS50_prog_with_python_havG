#let make cli-program to display meow (times of meow user enter) first by conventional method and then by argparser

import sys

if len(sys.argv) == 1:  # in case where user doesn't enter anything after file name
    print("Meow")   # it simply prints one meow
elif len(sys.argv) == 3 and sys.argv[1]=="-n":
    n= int(sys.argv[2])  #first converting the user entered number (after-n) into integer
    print("\n Meow!" * n)  #then printing 'Meow!' n times 
else:   # if user entered anyhing else kinda default case 
    print("Usage of Meow_cli.py: please enter in this format(ex:) \n python Meow_cli.py -n 4")
    
    
 