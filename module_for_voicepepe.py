def main(): # for testing porpose only 
    # here we're making the string variable in b/w its also contains 'cut' keyword 
    #whenever corsor encounters this keyword, during traversing this string before and after this keyword it will be build the two seperate sentences 
    # by combining those bunch of words before and after 'cut' keyword 
    txt= "Hello my name is Sphinix Herodotous. break I am here to test the pepe_say voice module, break this should be the last sentence of test-string: 'txt'."
    text_words = txt.split() # in this test string we're splitting it into numerous words
                      # each words now will be acts as element of the list which is going to be processed through dynamic_bubble function 
    
    #dynamic_bubble(lis_tobe_process=text_words)
    
    pepe_say(txt)
    
def dynamic_bubble(lis_tobe_process):
    
    #initializing two string list here
 
    msg_sentences = []
    temp_sentence = []
    for words in lis_tobe_process:
        if words == "cut": #here nl stands for newline (coder defined)
            # then we going to concatenated the temp_sentence list to msg_sentence list
            msg_sentences.append(" ".join(temp_sentence)) #join list means concatenating a list of strings with a specified delimiter to form a string.[here we use space as delimiter] not using coma as we're making sentence with all those words.
            #join() function to join a list of strings. This function takes iterable as argument or List is an interable, 
            # so we can use it with List. Also, the list should contain strings, 
            # if you will try to join a list of Ints then you will get an error message

            #now resetting the temp_sentence list for each time when we encounter newline 'nl'
            temp_sentence=[] 
        else:  # if we encouter the words other than new-line 'nl' then we simply append those words to temp-list 
            temp_sentence.append(words)

    # append last sentence if exit in temp_sentence list
    while temp_sentence: # while elements exists in temp list , untill then this while will be true,(but for one time; will will break it)
        msg_sentences.append(" ".join(temp_sentence))
        break
    # for displaying pepe saying requested mesaage ,first we have to call bubble-fn for corresponds to that specific message[which print the bubble containing our message], 
    # and then we have to print-pepe literally-ASCII to display it as he's saying the rquested message 

    res = max(msg_sentences, key = len)  # finding here the longest string-element in the msg_sentences string-list  [basically finding the sentence with maximum length]
    bubble_length = len(res) + 2  #  here we're set bubble length as 2 bit more longer than maximum-length sentence in string-list

    # now going to print message in bubble aesthetically
    print(f"""({"‾" * bubble_length})""")  # this is for printing upper-bubble-lines enclosed by round-brackets'(  )' [here used overline as a line]
    for i in range(len(msg_sentences)):     # now going to print successively each sentences from msg_sentences list (string-list)
      print(f"( {msg_sentences[i]}", end ="")   # note that we're not changing line here from printing trailing curly-lines 
      print(f"""{"~" * (len(res) - len(msg_sentences[i])+1)})""")   #here we're printing trailing curly-lines 
                                                                 #in way that the last round-bracket')' completely alligned with upper & lower bubble-lines
                               # logic is this "~" * (len(res) - len(split_msg[i])+1)     printing (len of longest sentence minus len of current sentence plus 1)-times curly-line 
    print(f"""({"_" * bubble_length})""") # this is for printing lower-bubble-lines enclosed by round-brackets'(  )' [here used underscore as a line]

def our_pepe():
    
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


def pepe_say(message):
    # Split the message/text into words first,,, so it can be processed further by dynamic_bubble fn 
    words = message.split()
    dynamic_bubble(lis_tobe_process=words)  # Call dynamic_bubble function with the list of words
    our_pepe()


if __name__ == "__main__":
    main()
