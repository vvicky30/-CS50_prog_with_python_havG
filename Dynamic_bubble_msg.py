from sys import argv

msg = argv[1:]  # first here we going to save the message given by user through command-line in this 'msg' var
print(msg)

split_msg= msg.split("/nl") #going to split the msg where we encountered the 'nl' stands for new-line(coder-defined)
                            #for after 'nl' and before 'nl' those bunch of words considered to be sentences 
                            # and here each sentences we going to store in split_msg-list as string-elements
'''

print(split_msg)
o/p:

if msg = "I am Sphinix Herodotous,/nlhaving traversed seven oceans,/nlI have arrived here solely to meet you,/nlmy lady"

['I am Sphinix Herodotous,', 'having traversed seven oceans,', 'I have arrived here solely to meet you,', 'my lady']
 
''' 
res = max(split_msg, key = len)  # finding here the longest string-element in the split_msg string-list  [basically finding the sentence with maximum length]
bubble_length = len(res) + 2  #  here we're set bubble length as 2 bit more longer than maximum-length sentence in string-list

# now going to print message in bubble aesthetically
print(f"""({"‾" * bubble_length})""")  # this is for printing upper-bubble-lines enclosed by round-brackets'(  )' [here used overline as a line]
for i in range(len(split_msg)):     # now going to print successively each sentences from split_msg (string-list)
  print(f"( {split_msg[i]}", end ="")   # note that we're not changing line here from printing trailing curly-lines 
  print(f"""{"~" * (len(res) - len(split_msg[i])+1)})""")   #here we're printing trailing curly-lines 
                                                             #in way that the last round-bracket')' completely alligned with upper & lower bubble-lines
                           # logic is this "~" * (len(res) - len(split_msg[i])+1)     printing (len of longest sentence minus len of current sentence plus 1)-times curly-line 
print(f"""({"_" * bubble_length})""") # this is for printing lower-bubble-lines enclosed by round-brackets'(  )' [here used underscore as a line]