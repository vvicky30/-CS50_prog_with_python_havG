# sometimes while unit-testing of module all its building block functions is working fine logically on purpose 
# but main-fn can be taking value (value of of type which is not compatible for functions to prcess)from user which is making further functions look like they're faulty

# on that scenerio how to use pytest 
def main():
    num = input("what's number") # here as developer forgot to constrain this input-function in taking only integer value 
                                #and somehow if user also entered non-integer value in this case if user entered string-type data
                                #then further square funvtion will throw type error not becuse square error is faulty but square-function passed with unsuitable datatype 
    print("your sqaured number is: ", sqr(num))

def sqr(n):
    return n*n

if __name__ == "__main__":
    
    main()

# as here if we enter some string for ex: sphinix it willl shrow error like this :
#return n*n
#           ~^~
#TypeError: can't multiply sequence by non-int of type 'str'
# its looking like our function is faulty but in actuality value is unsuitable to be squared as its not an integer 

