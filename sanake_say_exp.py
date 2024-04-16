# here this py script i created for experimenting regarding snake-say module authored by me , gona be making module by packaging the project as python module 
# which i m gona acess through-out my python in system even ouside that local folder of that particular project.

def main():
    
    PEPE =  r"""   \\                         \\ 
   \\                          \\
    \\                           \\
     \\⬜⬜⬜⬜⬜🐸🐸🐸🐸🐸🐸⬜🐸🐸\\⬜⬜⬜ 
    ⬜\\⬜⬜⬜🐸✅✅✅✅✅✅🐸✅✅🐸\\⬜⬜ 
    ⬜⬜\\⬜🐸✅✅🐸🐸🐸🐸🐸🐸✅🐸🐸🐸\\⬜ 
    ⬜⬜\\🐸✅✅🐸✅✅✅✅✅✅🐸✅✅✅🐸\\ 
    ⬜⬜⬜🐸✅✅✅🐸🐸🐸🐸🐸🐸✅🐸🐸🐸🐸🐸 
    ⬜⬜🐸✅✅✅🐸🐸⬜⬛⬛⬜🐸🐸⬜⬛⬛⬜🐸 
    ⬜🐸🐸✅✅✅🐸⬜⬛⬛⬛⬜🐸⬜⬛⬛⬛⬜🐸 
    🐸✅🐸✅✅✅✅🐸🐸🐸🐸🐸✅🐸🐸🐸🐸🐸⬜ 
    🐸✅🐸✅✅✅✅✅🐸🐸🐸✅✅✅🐸🐸🐸⬜⬜ 
    🐸✅✅✅✅✅✅✅✅✅✅🐸✅🐸✅✅✅🐸⬜ 
    ✅✅✅✅✅✅✅✅✅🐸🐸✅✅✅🐸🐸✅🐸⬜ 
    ✅✅✅✅✅✅✅✅✅🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 
    ✅✅✅✅✅✅✅🟥🟥🧰🧰🧰🧰🧰🧰🧰🧰🟥⬜ 
    🐸✅✅✅✅✅🟥🧰🧰🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 
    🐸✅✅✅✅🐸🟥🟥🟥🟥✅✅✅✅✅✅✅🐸⬜ 
    ⬜🐸✅✅✅✅🐸🐸✅✅✅✅✅✅✅✅🐸⬜⬜ 
    ⬜⬜🐸✅✅✅✅✅✅✅✅✅✅✅✅🐸⬜⬜⬜ 
    ⬜⬜⬜🐸🐸✅✅✅✅✅✅✅✅🐸🐸⬜⬜⬜⬜ 
    ⬜⬜⬜⬜⬜🐸🐸🐸🐸🐸🐸🐸🐸⬜⬜⬜⬜⬜⬜
    """ 
    print(PEPE)
    msg = """hello how are you vedant vfrvfrvrfvrfv defciewjfcpiefcpiewjfcepf"""
    
    bubble(msg)
    say(msg,PEPE)



# here we prepare out message box , which will contain the whichever mesaage user want to print
def bubble(message):
    bubble_length = len(message) + 2        # for better containing the requested mesaage we have to make box 2 bits-more long wrt the leangth of message[here this is upper-box-line]
    bubble_lines = message.split('\n')
    
    return f"""
{"_" * bubble_length}
[{message}]
{"‾" * bubble_length}"""                  # for better containing the requested mesaage we have to make box 2 bits-more long wrt the leangth of message[here this is lower-box-line]


# for displaying pepe saying requested mesaage ,first we have to call bubble-fn for corresponds to that specific message[which print the bubble containing our message], 
# and then we have to print-pepe literally-ASCII to display it as he's saying the rquested message 
def say(message, pepe):
    print(bubble(message=message))
    print(pepe)
    


main()