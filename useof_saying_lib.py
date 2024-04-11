# in this program we will import our own Sying_liberary and its affiliated modules which're imported specifically here from saying_liberary
from saying_lib import What_name
from saying_lib import greetings_to_name   # here imported greetings_to_name module specifically from saying_lib

user_name = What_name()
print(f"[NOTE: here we're using greetings module of saying-lib]:-\n {greetings_to_name(user_name)}")

'''
o/p (if in the liberary's source code we doesn't resolve the problem of unwanted calling of main-fn) [illustation-stage]:-
  {here we can see even though we imported what_name & greetings_to_name modules specifically its showing result of goodbye_to_name module/method as well}:

what's your good-name? 
[note: You can either enter your full-name(name with surname) or simply just enter the name only]   vedant
Hello  Vedant!!...[You Entered Name only] 
Welcome to our own 'Saying_liberary'
Goodbye Vedant!!...[You Entered Name only] 
Hope you use our 'Saying_library' soon
what's your good-name? 
[note: You can either enter your full-name(name with surname) or simply just enter the name only]vedant
[NoTE: here we're using greetings module of saying-lib]:-
 Hello  Vedant!!...[You Entered Name only]
Welcome to our own 'Saying_liberary'  



o/p (if in the liberary's source code we resolve the problem of un wanted calling of main-fn)[here you can see it doesn't showing goodbye_to_name]
what's your good-name? 
[note: You can either enter your full-name(name with surname) or simply just enter the name only]    ripudaman shaktaar
[NoTE: here we're using greetings module of saying-lib]:-
 Hello  Ripudaman Shaktaar!!...[You Entered Name alongwith Surname]
Welcome to our own 'Saying_liberary'
'''
