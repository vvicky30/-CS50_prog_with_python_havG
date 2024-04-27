# in this driver python-script we're going to  just specifically import the dynamic_bubble function from sanake_say_exp -module 
# to preview the msg-bubble only for containing the msg entered by user through cli.
from sanake_say_exp import dynamic_bubble
from sys import argv
def main():
    messae_cli = argv[1:]
    dynamic_bubble(messae_cli)
    


main()
'''
o/p:

CS50_pythonProg_hav> python  driver_bubble_msg.py Hello!! /nl I am PERSEUS /nl son of ZEUS /nl here i am for the conquest of the earth /nl i am not going to leave /nl untill unless i conquer /nl each and everthing completely.
(‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾)
( Hello!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)
( I am PERSEUS~~~~~~~~~~~~~~~~~~~~~~~~~~~~)
( son of ZEUS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)
( here i am for the conquest of the earth~)
( i am not going to leave~~~~~~~~~~~~~~~~~)
( untill unless i conquer~~~~~~~~~~~~~~~~~)
( each and everthing completely.~~~~~~~~~~)
(_________________________________________)

'''