# now here we're going to test main function of square_fine_main_buggy.py   as it's taking string value or not kinda 
from square_fine_main_buggy import sqr
# here also specifically we have to import pytest 
import pytest

def test_string_input():
    with pytest.raises(TypeError):
        # while testing with pytest if given testcase raised TypeError or not ?
        #when:
        sqr("Sphinix")
        
"""
o/p: (meaning success ; as its indeed raising TypeError means developer has to constrains input function)
 pytest test_square_fine_main_buggy.py
============================================================== test session starts ==============================================================
platform win32 -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0
rootdir: C:\Users\hp\PycharmProjects\CS50_pythonProg_hav
collected 1 item                                                                                                                                  

test_square_fine_main_buggy.py .                                                                                                           [100%] 

=============================================================== 1 passed in 0.04s =============================================================== 
"""