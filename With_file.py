with open("with_name.txt", "a") as file:
    
    
                                # appending file we're going to make with 'with' keyword
                                # as we all know with keyword used in python for using resources when it's nedded 
                                # once task completed resources will be disallocate to their respective spaces automatially , 
                                #so here we don't have to close file explicitly by mentioning in the code.
    file.write(input("what's that name you want to append in the file: With name?").strip().title())
    file.write("\n") # for changing cursor to new line 
                               