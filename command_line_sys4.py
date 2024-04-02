# another small exercise 
# for taking user-name alongwith surname 
# and raise error if it enter name without surname or doesn't enter the name 
# or raise error in situation if he/she enters something more byound name & surname 
import sys

if len(sys.argv)>3:
    # means alongwith file name of argv[0] and username on argv[1], surname on argv[2]
      # len should be less then 3 if its greater then raise error like this ;
    print("Too many args: please enter only user-name & surname")

# here inplace of print we can use sys.exit("Too many args: please enter only user-name & surname")
#as its used to exit from command-line console after printing that message to console
elif len(sys.argv)<3:
    print("Too few args: plz enter your user-name & surname as well")

else:  # if user perfectly enters everything 
    print(f"so your user-name is :{sys.argv[1]} and surname is: {sys.argv[2]} ")

'''
o/p(if user perfectly enters):
python command_line_sys4.py Sphynix herodotous
so your user-name is :Sphynix and surname is: herodotous

o/p (if user enter few args):
python command_line_sys4.py Sphynix           
Too few args: plz enter your user-name & surname as well

o/p (if user enter too many args):
python command_line_sys4.py Sphynix herodotous 456
Too many args: please enter only user-name & surname
'''
