#here first we are going to first defining main-fn wehre all driver code is going to exist for initial and final excecution , 
#where we're going to call several fns defined out of the main-fn by passing relevent arguments,parameters/var
#we're going to define our own sets or chains of fns out of the main-fn all with their operational definitions and with their functional parameters (optional parameters, necesaary parameters with default values etc), and then going to return the final furnished o/p from respective fns to corresponding functional call in main-fns


'''
https://www.geeksforgeeks.org/python-functions/

https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
'''
# Here i am going to make main fn along with user defined fns for dairy shop customers (Example)
import math
def main():
    welcome_to_dairy()
    customer_name = input("Can you please tell us your good-Name: ")
    customer_name = formatting_name(customer_name)
    milk_lit = float(input(f"Nice to meet you {customer_name} \nplease tell us how many litres of milk do you want? \n[NOTE: 66.87 rs per litre Milk] "))
    print(f"So {customer_name} you ordered: {milk_lit} litres of milk \nyou have to pay total: {milk_cost(milk_lit)} rs")
    goodbye_customer(customer_name)


def welcome_to_dairy(): 
    
    print("Hey there!...\nWelcome to Śrī Śyāmā Dairy, \nWe’re thrilled to have you.")
    
    
def goodbye_customer(name="customer"): #defualt name will be customer
    print(f"goodbye {name} \nWe look forward to seeing you again.")
    

def formatting_name(name="customer"): #default name will be customer, in case if customer not coperating with us 
    return(name.strip().title()) # here we're removing extra whitespaces in the left and right of the string alonwith capitalizing them.


def milk_cost(litre= 0):  # here setting default litre zero as cost of it will be also zero , when it multiplied by unit amount
    unit_cost = 66.87
    litre_cost= litre*unit_cost
    def rounding_up_cost(l_cost = 0, deci_p=0):  # here we define another fn for rounding_up porpose within another user defined fn(here its: milk_cost)
        ten_raised_to_p = 10**deci_p
        return(math.ceil(l_cost*ten_raised_to_p/ten_raised_to_p)) # using ceil for rounding up money to take little-bit advantage ot customer
    final_cost= rounding_up_cost(litre_cost) #here deliberately not fill deci_p as by default it will start to round up from zero-decimal-pt or round up for 'paise'
    return(f"{final_cost:,}") # for currency formatting for bigger amounts 
        
main() # calling main fn to excecute drive code where all sets of user defined fns called for corresponding tasks    
    
'''
Hey there!...
Welcome to Śrī Śyāmā Dairy,
We’re thrilled to have you.
Can you please tell us your good-Name:        Sphinix herodotous
Nice to meet you Sphinix Herodotous
please tell us how many litres of milk do you want?
[NOTE: 66.87 rs per litre Milk] 450
So Sphinix Herodotous you ordered: 450.0 litres of milk
you have to pay total: 30,092 rs
goodbye Sphinix Herodotous
We look forward to seeing you again.
'''   
