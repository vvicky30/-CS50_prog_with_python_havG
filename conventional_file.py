#here we're going make program of simple file input/output both in wtiting and appending permission.

name = input("what's your name [write alongwith surname]: ").strip().title()

#file = open("name.txt", "w")  # here open is standard function used for opening the file or resources , 
                                         # here 'open' will open the file named 'name.txt' if file existed already , 
                                         # if not then it will make file with this name and open it with "w"(write permission)
        # this procedure of opening file with write permission has one limitation , as each time if we open file with this "w" permission then each time it will overwrite on the last saved data.
file= open("name.txt", "a")  # as we dont want to overwrite on our last saved data , so here we're going to open file with append "a" permission for maintaining list of names in the file         
file.write(f"{name} \n")  # going to write name and then on new line we want to move our cursor
file.close()# its compulsory to close a file once we're finished iteracting with file, otherwise file will be possibely currupted.




# as above discuss that why it's necessary to close file ....on that same tangent without bieng consious about closing the file 
# there's another method to open file in a way that once a file open (in any permission mode ) and then once a user completed iteracting (appending,writing  & reading etc ) with file ,
#by using this method , it will automatially close the file , we don't have to mention in a code for it, explicitly.
#[refer to file: With_file.py]