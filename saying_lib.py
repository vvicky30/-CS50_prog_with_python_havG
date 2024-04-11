# going to make our own liberary/module of python that will be used by us here locally by importing into another project 
# or program or we can simply upload it on cloud-server so that it can acess by contributor on that server or on that same infra-level
#or we can contribute to open-source liberary-hub or repository or like PYPI web-site for open source contributors for python. 
   # so that from there various users across the globe can install our liberary through pip or by other ways and use it for repective purposes.
   
# here i am going to make a liberary and name of that liberary is simply the name of this python file which's 'saying_lib'

#all these for checking purposes we have to create here  main fn as well. 
def main():
    
  yourName = What_name()
  print(greetings_to_name(yourName))
  print(goodbye_to_name(yourName))



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
   

# for illustation purposes 
#main() # illustration-stage

# now our liberary is complete here, but there's one catch and that catch is whhen while importing this saying-liberary,
# specifiaclly while doing that we import greetings_to_name module only to another program for making greetings msgs to specified name 
# then it ultimately initiate method greetings_to_name as well as the goodbye method for that specified name 
# as behind the scene after importing saying-liberary's module (here greetings_to_name) python interepretor starts reading from left to right and top to bottom,
# where it eventually encountered with main()[main-fn]-calling in which both methods called for testing purposes , 
# and that's the reson while importing specific modulle/method (here greetings_to_name) from saying-lib still in that program it will call all the methods corresponds to main-fn definition where we call each module.
# so for resolving this problem we have to specify that while importing each module for respective task we shouldn't excecute main-fn in liberary's source code.
# so here in liberary's source code we have to specify that when main should be excecute and when is not 

# here 's the way to specify that 
if __name__ == "__main__" :   # it means if we excecute this file which's source-code of saying-liberary through commandline simply then name will be equals to "main" [condtion will be true]
                             # and this main will excecute if this source-code execute through importing it in another program then name will not be equals to 'main' and this main(lib's source-code main will not be execute). 
   main()

   