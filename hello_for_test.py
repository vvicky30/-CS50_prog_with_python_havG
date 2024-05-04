

def main():
    name= input("what's your name").strip().title()
    print(hello(name))

def hello(to = "World"): # passing default value string World, if name specifically not passed 
     #print(f"hello {to} ") # remeber while defining functions its preferrable to return value instead of using printfn like this , 
                          #'coz this print fn not going to return values that can be tested agaisnt test-cases using test_script , print fn used for bypass output only.
                           
     return f"hello, {to}"

if __name__ =="__main__":
    main()
