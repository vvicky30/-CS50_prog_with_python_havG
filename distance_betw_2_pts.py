
import math
#for taking input from user:
print("plz,enter cordinates of 1-point:" )
X1=float(input())
Y1=float(input())
print("now,Enter the cordinates of 2-point:")
X2=float(input())
Y2=float(input())

# Function to calculate distance 
def Dist_Btw_points(x1 , y1 , x2 , y2): 
  
    # Calculating distance 
    return math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)   #according to mathematical formlula := (X2-X1)^2 + (y2-y1)^2 *1.0(reamains-float)

      
# Drivers Code 
print("distance between two points is","%.6f"% Dist_Btw_points(X1, Y1, X2, Y2)) #.6f for allowing atmost 6 decimal-values
  