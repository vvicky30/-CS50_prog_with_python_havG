

def main():
    name= input("what's your name").strip().title()
    hello(name)

def hello(to = "World"): # passing default value string World, if name specifically not passed 
    print(f"hello {to} ")
    

if __name__ =="__main__":
    main()
