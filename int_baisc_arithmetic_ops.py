# approach-1 (less compact)
a=input("enter value of 'a': ")
b=input("enter value of 'b': ")
#here we taking reponses from user as a string even if they're entering numericals (it alwys treated a string by default by input fn here untill unless it will be converted to integer thrigh int-fn)
c= int(a)+int(b)
print(c)

#approach-2 (more comapact) will be nesting the whole input-fn within int-fn 
# this only allowed user to inout numbers that will eventually be treated as int here
d=int(input("enter value of 'd': "))
e=int(input("enter value of 'e': "))
print(d+e)

#approach-3 (most compact)
print(int(input("enter the value of 'p': "))+int(input("enter the value of 'q': ")))
