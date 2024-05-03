# as in last python_script named as testby_assertion_sqr.py we unit_tested fine_square & broken_square fns of square_clc.py module 
# but as we can see in that it's very very time consuming and complex to handle respective AssertionError raised by corresponding aseertion statement, 
# for handling  all these errors we have to try and except each time for each possible test cases manually. and it's very leanthy..
# so what should we do now ... we will use pytest (a third-party python package ) through that package we're going to run all those assertion statement 
# direcly by running python script full of those assertion statement  with pytest package , 
# this package under the hood automatically try and except AssertionError, handle output and preview failed and successful test-cases in very readable manner.

# so while using pytest package for running unit-testing python script full of assertion statements developer has nothing to worry about trying and exception handling and which test-cases failed precisely.
#all this will be handle by pytest framework behind the scene and it will give us fauilure(F), sucess(.) status corresponds to category of test-cases and 
#what're those test-cases specifically failed in each test-case category

# with this much help from pytest, developer can focus on the actual essence of unit-testing ...instead of strcturing and wasting time on orchestrating sourcecode of unit-test script manually.

# first install pytest using pip

from square_clc import fine_square, broken_square


# test-cases categorized by function for which they're goin to use :-

def test_fine_sqr():
    assert fine_square(11) == 121
    assert fine_square(99) == 9801
    assert fine_square(49) == 2401
    assert fine_square(199) ==39601

def test_broken_sqr():
    assert broken_square(11) == 121
    assert broken_square(99) == 9801
    assert broken_square(49) == 2401
    assert broken_square(199) ==39601

#test cases categorized in negatives, postives, Zeros for each function going to be unit-tested here :-    
def test_positives_fine_sqr():
    assert fine_square(2) == 4
    assert fine_square(3) == 9
    assert fine_square(4) == 16
    assert fine_square(5) == 25
    
def test_negatives_fine_sqr():
    assert fine_square(-2) == 4
    assert fine_square(-3) == 9
    assert fine_square(-4) == 16
    assert fine_square(-5) == 25

def test_positives_broken_sqr():
    assert broken_square(2) == 4
    assert broken_square(3) == 9
    assert broken_square(4) == 16
    assert broken_square(5) == 25
    
def test_negatives_broken_sqr():
    assert broken_square(-2) == 4
    assert broken_square(-3) == 9
    assert broken_square(-4) == 16
    assert broken_square(-5) == 25
      
def test_zero_fine_sqr():
    assert fine_square(0)==0
    
def test_Zero_broken_sqr():
    assert broken_square(0)==0

# test cases by looping from -10 to 10 for each fns here. :-    

def test_loop_negpos_finesqr():
    for i in range(-10,10):
        assert fine_square(i) == i*i

def test_loop_negpos_brokensqr():
    for i in range(-10,10):
        assert broken_square(i) == i*i

#remember always...that name of test_cases_category (here Function-name) within test_script (the test-script which's going to run by pytest) 
# in this manner: 'test_*.py' (here for ex: test_loop_negpos_brokensqr()) so that pytest  can automatically discover and execute your test-cases within that test_cases_category or function.
# even we have to name out test_script file in this manner only (here for ex: test_assertion_sqr.py) so that this test_script file can be recognized by pytest for executing various test-cases in it. 
'''
o/p of running commnad 'pytest  test_assertion_sqr.py':-         
[we can use command like this 'pytest -v test_assertion_sqr.py' we can run pytest with the -v (verbose) option. 
This will provide more detailed output, including the names of all test functions as they are executed and the results of each individual test case.]
     
PS C:\Users\hp\PycharmProjects\CS50_pythonProg_hav> pytest  test_assertion_sqr.py  

============================================================== test session starts ==============================================================
platform win32 -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0
rootdir: C:\Users\hp\PycharmProjects\CS50_pythonProg_hav
collected 10 items

test_assertion_sqr.py .F..FF...F          //here '.' represents sucess of testcases corresponds to that test_case_category or function (in our case)  whereas 'F' stands for Failure in same context.                                                                                                 [100%]

=================================================================== FAILURES ==================================================================== 
________________________________________________________________ test_broken_sqr ________________________________________________________________ 

    def test_broken_sqr():
>       assert broken_square(11) == 121
E       assert 22 == 121
E        +  where 22 = broken_square(11)

test_assertion_sqr.py:28: AssertionError
___________________________________________________________ test_positives_broken_sqr ___________________________________________________________ 

    def test_positives_broken_sqr():
        assert broken_square(2) == 4
>       assert broken_square(3) == 9
E       assert 6 == 9
E        +  where 6 = broken_square(3)

test_assertion_sqr.py:48: AssertionError
___________________________________________________________ test_negatives_broken_sqr ___________________________________________________________ 

    def test_negatives_broken_sqr():
>       assert broken_square(-2) == 4
E       assert -4 == 4
E        +  where -4 = broken_square(-2)

test_assertion_sqr.py:53: AssertionError
__________________________________________________________ test_loop_negpos_brokensqr ___________________________________________________________ 

    def test_loop_negpos_brokensqr():
        for i in range(-10,10):
>           assert broken_square(i) == i*i
E           assert -20 == (-10 * -10)
E            +  where -20 = broken_square(-10)

test_assertion_sqr.py:72: AssertionError
============================================================ short test summary info ============================================================ 
FAILED test_assertion_sqr.py::test_broken_sqr - assert 22 == 121
FAILED test_assertion_sqr.py::test_positives_broken_sqr - assert 6 == 9
FAILED test_assertion_sqr.py::test_negatives_broken_sqr - assert -4 == 4
FAILED test_assertion_sqr.py::test_loop_negpos_brokensqr - assert -20 == (-10 * -10)
========================================================== 4 failed, 6 passed in 0.20s ========================================================== 
'''
