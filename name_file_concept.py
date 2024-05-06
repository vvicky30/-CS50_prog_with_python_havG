name = [] # name list initialized
# for loop for taking 5 names from users and save them in the name list 

for i in range(5):
    
    name.append(input("So, what's your name? [enter alongwith surname]: ").strip().title())
    
print("Here is the list of Names:",name)
#for loop for printing greetings to each name in the list 
for names in name:
    print(f"Hello..{names} Nice to meet you")
    
# here this program for illustrating the use cases file input/output 
# As here we can see once we close this program out all the names which we saved in the name-list will be wiped out certainly , 
# as all the variables and constant values alongwith values we set for variables to be processed is saved in current dedicated chunk of RAn-memory
# which's volatile in nature as all the data is saved in this memory for temprory purposes(untill/unless IDE or major task thread going-on related to current program)
# thats where storing data in file through pythons' standard file input/output procedure is significant.

#[now refer to file: conventional_file.py]

