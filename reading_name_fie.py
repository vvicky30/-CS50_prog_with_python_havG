with open("with_name.txt") as file:
          # as opening file without passing reading/appending/writing permisssion is going to be open with reading permission bydefault.
    line = file.readlines()
                              # here we're saving all readed lines from file in line variable , 
                              #but the catch is it also reads the new-line "/n" as its used by us for saving each names in each line 
                              # here while reading cursor do the same and during priniting them each with print-fn under for loop its adds extra new-line space.
                              # so getting ridd off that extra new line space we're going to use rstrip-fn.

#print(line) as this will return all the names written in the file in the form of list 
# as you can see here like this : ['   Skrillix hellios\n', ' helmand kilochock\n', 'Sphinix Herodotous\n', 'Precarious Ferriera\n', 'Crolina Camroon\n']
# with \n symbol 
#now going to print each names from line variable line by line ...going to remove extra newline space , as there's \n already from file as we can see above 
for lines in line :
    print(lines.rstrip())
    
    
print("---------more compact approach to reading lines from file:")
with open("with_name.txt") as file:
    for lines in line :
        print(lines.rstrip())
        
'''
o/p:
 Skrillix hellios
 helmand kilochock
Sphinix Herodotous
Precarious Ferriera
Crolina Camroon
---------more compact approach to reading lines from file:
   Skrillix hellios
 helmand kilochock
Sphinix Herodotous
Precarious Ferriera
Crolina Camroon
'''