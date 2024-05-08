# now going to read the data from a file line by line and sorted them with the help of list and then print them.
# generally in this way we can make several manipulation-operation over data  by first reading them from file and then manipulating them according to our purposes, and print them
name_lis = []
with open("with_name.txt") as file :
    line = file.readlines()
    for lines in line :
        name_lis.append(lines.rstrip())
    
# now  going to print in sorted way 
for names in sorted(name_lis):
    print(f"Hello, {names}")  # with greetings 


print("-------there's another approach as well..we can direclt sorted file as well")# this approach not that much prefeeered by developers 
                                                                                   #as in above approach is more open to costomization and manipulation of data , once read from respective files.

with open("with_name.txt") as file :
    for lines in sorted(file):
        print(lines.rstrip())
        
'''
o/p:
Hello,    Skrillix hellios
Hello,  helmand kilochock
Hello, Crolina Camroon
Hello, Precarious Ferriera
Hello, Sphinix Herodotous
-------there's another approach as well..we can direclt sorted file as well
   Skrillix hellios
 helmand kilochock
Crolina Camroon
Precarious Ferriera
Sphinix Herodotous
'''