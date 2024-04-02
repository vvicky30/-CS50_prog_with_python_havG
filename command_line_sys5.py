#another example just like the last one in command_line_sys4.py file 
# for allowing username to enter name alonwith surname throught commandline 
# but here for aesthetic terms we going to use cowsay package to greet user with his name if he/she enters name properly

import cowsay
import sys
if len(sys.argv)>3:
    # means alongwith file name of argv[0] and username on argv[1], surname on argv[2]
      # len should be less then 3 if its greater then raise error like this ;
    cowsay.tux("Too many args: please enter only user-name & surname")

elif len(sys.argv)<3:
    cowsay.turtle("Too few args: plz enter your user-name & surname as well")

else:  # if user perfectly enters everything 
    cowsay.cow(f"Hello!: {sys.argv[1]}-{sys.argv[2]}, i am COW, MOO..MOO! ")


'''
o/p(if user perfectly enters):
python command_line_sys5.py Sphynix herodotous
  _______________________________________________
| Hello!: Sphynix-herodotous, i am COW, MOO..MOO! |
  ===============================================
                                               \
                                                \
                                                  ^__^
                                                  (oo)\_______
                                                  (__)\       )\/\
                                                      ||----w |
                                                      ||     ||


o/p (if user enter few args):
  _________________________________________________
 /                                                 \
| Too few args: plz enter your user-name & surname  |
| as well                                           |
 \                                                 /
  =================================================
                                                   \
                                                    \
                                                     \
                                                      \
                                                                                 ___-------___
                                                                             _-~~             ~~-_
                                                                          _-~                    /~-_
                                                        /^\__/^\         /~  \                   /    \
                                                      /|  O|| O|        /      \_______________/        \
                                                     | |___||__|      /       /                \          \
                                                     |          \    /      /                    \          \
                                                     |   (_______) /______/                        \_________ \
                                                     |         / /         \                      /            \
                                                      \         \^\\         \                  /               \     /
                                                        \         ||           \______________/      _-_       //\__//
                                                          \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                                                            ~-----||====/~     |==================|       |/~~~~~
                                                             (_(__/  ./     /                    \_\      \.
                                                                    (_(___/                         \_____)_)


o/p (if user enter too many args):
 _________________________________________________
 /                                                 \
| Too many args: please enter only user-name & surn |
| ame                                               |
 \                                                 /
  =================================================
                                                      \
                                                       \
                                                        \
                                                         .--.
                                                        |o_o |
                                                        |:_/ |
                                                       //   \ \
                                                      (|     | )
                                                     /'\_   _/`\
                                                     \___)=(___/

'''