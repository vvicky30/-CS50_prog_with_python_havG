print("hello, vedanta")
print("hello, dre")
#here as you can see python developers for providing us the elements or samll fn to print or preview somthing on console or terminal 
#whereas the previewing string , numbers , picture, matrices is up to the programer's intent which we generally called it as 'side effects' here

#if here in prog. we have to ask sombody a quetion like this 
input("what's your name buddy?")
print("oh! hello Vedanta nice to chat with you")# as we already his/her name to be expected as something, for predecided(static) responses

#but for dynamic resposes here's the solution :
name = input("can you please tell your name? ")# here we're asisigning input fn's value to the variable here
# this variable will contian the user's response in string 
# then here we print the variable value(whic's the user's name here) in between the greetings expression 
print("hello, "+name+" nice to chat with you ")# here print-fn uses one argument
#here '+' also used for string concatenation 
print("hello, nice to meet you,",name)# here print-fn uses two argument one within quotes and other taking var-'name' here as arg.

# remember that each succesive print-fn always presume to be print var-values or literal/strings or anything from newline cursor.
# for making cursor to print on new-line we can use '\n' to end exisiting line and then start print from new line.
print("hello nice to meet you buddy, ", end=" ")# here we're not changing cursor to the newline , that's why 'end' here passed with empty quotes
print(name)

print("hello nice to meet you buddy, ", end="\n") #here we're going to print name on new-line by passing 'end' with '\n'
print(name)


#first commit