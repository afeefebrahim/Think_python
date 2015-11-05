#Use incremental development to write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go.

import math
def hypotenuse(s1,s2):
    h = math.sqrt(s1**2+s2**2)
    return h
print hypotenuse(6,7)
