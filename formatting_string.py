#asking user their name 
name = input("can you tell me your name buddy?")
print(f"hello, {name}")# here we're using the curly brackets for passing 'name' var.
# basically this gives idea to interpreter to read it as speacial or formatted string where 'f' here refers to formatting actions

#what if user we're dealing with is not coperating with us(developers)
# what if user intentionally/unintentionally add some of the random spaces before and after words 
#what if user randomly write their names-surnames in non-caps etc...
# for solving all of these kinds of issues we have to use several built-in fn comes with string-datatype
name1=input("Hey rude-boi! just tell me your name ")

name2=name1.strip()# here we're using strip-fn with no args passed, for ignoring whitespaces while printing string from right to left 

name3=name2.capitalize()#here we're using capitalize fn to capitalize string but here this fn only capitalize last word while printing from right to left(here it capitalize name only while surnames remained in default)

name4=name3.title()# here this title fn will resolve above partial capitalising prblm, it will treat the whole inputted string as title eventually capitalize whole string- names alongwith surnames

print(f"hello rude boi!, {name1}")# intermediate o/p-1
print(f"hello rude boi!, {name2}")# intermediate o/p-2
print(f"hello rude boi!, {name3}")# intermediate o/p-3
print(f"hello rude boi!, {name4}")#fully furnished string is here
# as you can see here we're using here various inbuilt fns of string for furnishing input-string one by one and saving intermediate o/p(s) to several string-var and finally printing the one fully furnished string. 

# this approach is too much time consuming for us developers so we should combine-up or chain-up this all inbuilt-fn ,eventually our code will seems more compact.

#approach 1
rude_boi_name= input("hey rude-boi, just tell me your name ")
rude_boi_name= rude_boi_name.strip().title()
print(f"hello rude-boi, {rude_boi_name} nice to treat you!")
#approch 2 (more compact)
rude_boi=input("hey rude-boi, just tell me your name ").strip().title()
print(f"hello rude-boi, {rude_boi} nice to treat you!")


#here we're noe going to use split -fn for spliting the input string in first and last name or can be used for any other porpuses where we have to split string whether from whitespaces or from any specific char

rude_first_name, rude_last_name= input("hey rude-boi, tell me your first a& last name").strip().title().split(" ")
#as here we can see i am spliting the input string from the whitespaces encounter , that's why we're passing ' " " ' this one white sapce as arg in split-fn 
print(f"hello rude-boi, here's your first name: {rude_first_name} and here's your last name: {rude_last_name}")

#here we're going to split verb from 'ing' from  using  split 
verb, ing_form = input("tell me any verb with ing from i.e. walking, making & starting, etc ").split("i")
print(f"so here we splitted your verb: {verb} and 'ing'-form: {ing_form}")

