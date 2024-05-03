# here we're going to unit_test both fn: fine_square & broken_square of sqare_clc module  through assertion -technique
# this technique relatively more compact than conventional if-statement testcases-technique, evne this this technique is not that compact , but time consuming 
# and less preferred by developers 

from square_clc import fine_square, broken_square

def main():
    #simple_assertion()
    assertion_and_exception()
    
def simple_assertion():
    #test-cases for fine square:
    assert fine_square(2) == 4
    assert fine_square(3) == 9
    assert fine_square(5) == 25
    assert fine_square(-4) == 16
    assert fine_square(0) == 0
    
    #test-cases for broken square:
    assert broken_square(2) == 4
    assert broken_square(3) == 9
    assert broken_square(5) == 25
    assert broken_square(-4) == 16
    assert broken_square(0) == 0
 # here this 'assert' is standard keyword of python which checks whether following statement is true.
 # here it checks whether operands(such as :2,3,-4,5 and 0) processed through operators (here fns like fine & broken square) is euqal to asserting value or not.
 # if these statements is not equal to their respective asserting value then this 'assert' keyword will raise AseertionError
 # it gives developer a idea that which function is buggy and which function is buggy for which value etc.

#here in this 'simple_assertion' fn there's one problem once interpreter encountered with one Assertion error 
# its then terminate whole program and we will end-up unchecked other test-cases.

         
# now we're going to handle all those ASSertion Error respectively with try and except statement 
    
def assertion_and_exception():
    #test-cases for fine square:
    try:   
        assert fine_square(2) == 4 , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually fine_square(2): {fine_square(2)}")
    try:   
        assert fine_square(3) == 9 , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually fine_square(3): {fine_square(3)}")
    try:   
        assert fine_square(5) == 25 , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually fine_square(5): {fine_square(5)}")
    try:   
        assert fine_square(-4) == 16 , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually fine_square(-4): {fine_square(-4)}")
    try:   
        assert fine_square(0) == 0 , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually fine_square(0): {fine_square(0)}")
    
    #test-cases for broken_square:
    try:   
        assert broken_square(2) == 4  , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually broken_square(2): {broken_square(2)}")
    try:   
        assert broken_square(3) == 9  , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually broken_square(3): {broken_square(3)}")
    try:   
        assert broken_square(5) == 25  , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually broken_square(5): {broken_square(5)}")
    try:   
        assert broken_square(-4) == 16 , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually broken_square(-4): {broken_square(-4)}")
    try:   
        assert broken_square(0) == 0 , "ASSERTION-ERROR"    # here we costomized name of error
    except AssertionError as e:
        print(f"{e}:Here actually broken_square(0): {broken_square(0)}")

    
    

main()

'''
o/p of 'simple assertion'-fn:
 
    assert broken_square(3) == 9
           ^^^^^^^^^^^^^^^^^^^^^
AssertionError
'''    
'''
o/p of 'assertion_and_exception'-fn:
ASSERTION-ERROR:Here actually broken_square(3): 6
ASSERTION-ERROR:Here actually broken_square(5): 10
ASSERTION-ERROR:Here actually broken_square(-4): -8

'''  