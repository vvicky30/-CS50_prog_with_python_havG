# so here we're going to unit-test sqaure fns through convenstional method which's not recommended( for developers) it's quite manual and typically less compact, time-consuming.
# here we used general if statement to test square fns with test-cases.

from square_clc import fine_square , broken_square
# import both function on which we're going to perfrom the unit-testing 

def main():
    conven_sqr_test()
    
    


def conven_sqr_test():  # for test-case value like 2 and 3 only
    #test cases for fine_square 
    if fine_square(2) != 4:
        print("fine_square function is buggy for value 2")
        print("fine_square(2): ", fine_square(2))
    if fine_square(3) != 9:
        print("fine_square function is buggy for value 3")
        print("fine_square(3): ", fine_square(3))
    if fine_square(5) != 25:
        print("fine_square function is buggy for value 5")
        print("fine_square(5): ", fine_square(5))
    if fine_square(-4) != 16: #-negative value
        print("fine_square function is buggy for value -4")
        print("fine_square(-4): ", fine_square(-4))
    if fine_square(0) != 0: #-zero value
        print("fine_square function is buggy for value Zero")
        print("fine_square(0): ", fine_square(0))
    
    #test cases for broken_square
    if broken_square(2) != 4: 
        print("broken_square function is buggy for value 2")
        print("broken_square(2): ", broken_square(2))
    if broken_square(3) != 9:
        print("broken_square function is buggy for value 3")
        print("broken_square(3): ", broken_square(3))
    if broken_square(5) != 25:
        print("broken_square function is buggy for value 5")
        print("broken_square(5): ", broken_square(5))
    if broken_square(-4) != 16: # for negative value 
        print("broken_square function is buggy for value -4")
        print("broken_square(-4): ", broken_square(-4))
    if broken_square(0) != 0: # for Zero
        print("broken_square function is buggy for value Zero")
        print("broken_square(0): ", broken_square(0))

main()

'''
o/p:
broken_square function is buggy for value 3
broken_square(3):  6
broken_square function is buggy for value 5
broken_square(5):  10
broken_square function is buggy for value -4
broken_square(-4):  -8
'''
