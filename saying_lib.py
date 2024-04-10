# going to make our own liberary/module of python that will be used by us here locally by importing into another project 
# or program or we can simply upload it on cloud-server so that it can acess by contributor on that server or on that same infra-level
#or we can contribute to open-source liberary-hub or repository or like PYPI web-site for open source contributors for python. 
   # so that from there various users across the globe can install our liberary through pip or by other ways and use it for repective purposes.
   
# here i am going to make a liberary and name of that liberary is simply the name of this python file which's 'saying_lib'


def What_name():
   name_lis =[] # initialized name-list which will fetch name and surname as well(if entered by user )
   name_lis = input("what's your good-name? \n[note: You can either enter your full-name(name with surname) or simply just enter the name only]").strip().title().split(" ")
                           # here we first used strip-fn which will strip-out all white_spaces behind name and beyond surname (in case user is not coperating).
                           # then we used title to capitalize the first word of name and surname 
                           # then we used split-fn with arguments pass one-whitespace, means if it encountered one whitespace it will split the string and seperately saved to name_list here.
   return name_lis                       
      
def greetings_to_name(name):
   if len(name) < 2: #meaning if list only consists of name but not surname
      return(f"Hello  {name[0]}!!...[You Entered Name only] \nWelcome to our own 'Saying_liberary'")
   elif len(name) == 2 : # meaning if list consist of name & surname both
      return(f"Hello  {name[0]} {name[1]}!!...[You Entered Name alongwith Surname] \nWelcome to our own 'Saying_liberary'")
   else:
      # means if user enter it full name that goes beyond 2 length then here we will greet him with his entered full name whatever he/she enter
           # its going to stored in name-list and we're going to print each element of the string list in same lines without bracket and commas
             # for this we're going to use for loop
      print("Hello", end=" ")
      for full_n in name:
         
         print(full_n, end = " ") 
         
      return("!!...[You Entered Your Full-Name] \nWelcome to our own 'Saying_liberary'")   
   
def goodbye_to_name(name):
   if len(name) < 2: #meaning if list only consists of name but not surname
      return(f"Goodbye {name[0]}!!...[You Entered Name only] \nHope you use our 'Saying_library' soon")
   elif len(name) == 2 : # meaning if list consist of name & surname both
      return(f"Goodbye {name[0]} {name[1]}!!...[You Entered Name alongwith Surname] \nHope you use our 'Saying_library' soon")
   else:
      # means if user enter it full name that goes beyond 2 length then here we will greet him with his entered full name whatever he/she enter
           # its going to stored in name-list and we're going to print each element of the string list in same lines without bracket and commas
             # for this we're going to use for loop
      print("Goodbye", end=" ")
      for full_n in name:
         
         print(full_n, end = " ") 
         
      return("!!...[You Entered Your Full-Name] \nHope you use our 'Saying_library' soon")   
   
    
yourName = What_name()
print(greetings_to_name(yourName))
print(goodbye_to_name(yourName))