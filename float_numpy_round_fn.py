import numpy as np 

float_arr = [1.24, 35.689, 4.78, 8.67]

rounded_arr = np.round(float_arr,)
print(rounded_arr)
rounded_arr1= np.round(float_arr, 2) # up to 2 decimal points 
print(rounded_arr1)

#or approach 2
# Creating an numpy array
arr = np.array([1.234, 2.567, 3.789])
 
# Rounding each element to the nearest integer
rounded_NParray = np.round(arr)
 
# Rounding each element to two decimal places
rounded_Nparray2 = np.round(arr, decimals=2)
 
# Displaying the results
print("Nearest integer:", rounded_NParray)
print("Decimal places:", rounded_Nparray2)

'''
[ 1. 36.  5.  9.]
[ 1.24 35.69  4.78  8.67]

Nearest integer: [1. 3. 4.]
Decimal places: [1.23 2.57 3.79]
'''
