import math
def square_root(a,x):
  y=0
  c=0
  for i in range(a):
    if x==y:
      c = x
    else:
      y = x+i/x
      x = y 
    s=math.sqrt(i)
    d = s-c
    print s,c,d  
n =square_root(9,3)
