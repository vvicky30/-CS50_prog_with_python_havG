#here we're going to make parity function for illustrating use-cases of single liner if-else conditionals
def main():
    number = int(input("enter number that you wanto parity-check: "))
    
    if is_even(number): # this will execute if is_even fn returns True boolean value
        print(f"yes, the given number: {number} is Even [parity checked by approach-1]")
    else:
        print(f"No, the given number: {number} is odd [parity checked by approach-1]")
        
    if is_even2(number):
        print(f"yes, the number: {number} is Even [parity checked by approach-2]")
    else:
        print(f"No, the given number: {number} is odd [parity checked by approach-2]")
        
    if is_even3(number):
        print(f"yes, the number: {number} is Even [parity checked by approach-3]")
    else:
        print(f"No, the given number: {number} is odd [parity checked by approach-3]")

#approach-1:
def is_even(n): #defining parity check function  
  
     if n % 2 == 0:
         return True
     
     else:
         return False
#approch-2 (Tighter one)         
def is_even2(n): #defining parity check function
    
    return True if n % 2 == 0 else False

#approch-3 (Tightest one)         
def is_even3(n): #defining parity check function
    
    return n % 2 == 0 # if this boolean expression is True then its ultimately returns true which excecutes corrrsponding If-block above
     # if this boolean expression return false evnetually its  corresponding IF block will not excecute , else-block will excecuted instead
     
main()

'''
o/p
For even-num-case:
enter number that you wanto parity-check: 48
yes, the given number: 48 is Even [parity checked by approach-1]
yes, the number: 48 is Even [parity checked by approach-2]
yes, the number: 48 is Even [parity checked by approach-3]

o/p
for off-num-case:
enter number that you wanto parity-check: 31
No, the given number: 31 is odd [parity checked by approach-1]
No, the given number: 31 is odd [parity checked by approach-2]
No, the given number: 31 is odd [parity checked by approach-3]
'''
