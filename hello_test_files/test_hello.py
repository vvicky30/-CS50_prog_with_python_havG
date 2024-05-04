from hello_for_test import hello

def test_default():
    assert hello() == "hello, World"
    
def test_passedname():
    assert hello("Sphinix") == "hello, Sphinix"

# here we're going to run this test script outside this package folder 'hello_test_files'  
# and going to run like this : pytest hello_test_files       ##here pytest automatically recognised the "hello_test_files" folder as python package 

'''
o/p: [both sucessful]
PS C:\Users\hp\PycharmProjects\CS50_pythonProg_hav> pytest hello_test_files
============================================================== test session starts ==============================================================
platform win32 -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0
rootdir: C:\Users\hp\PycharmProjects\CS50_pythonProg_hav
collected 2 items

hello_test_files\ test_hello.py ..                                                                                                          [100%]

=============================================================== 2 passed in 0.33s =============================================================== 
'''