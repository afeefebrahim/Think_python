from swampy.TurtleWorld import*
import math
def square(t,lenght):

  for i in range(4):
      fd(t, lenght)
      lt(t)
def polygon(t,lenght,n,angle):
   for i in range(n):
     fd(t,lenght)
     lt(t,angle)
def circle(t,r):
    arc (t,r,360)
    #circumference =2 * math.pi * r 
    #n = int(circumference/4)+1
    #lenght = circumference/n
    #step_angle = 360/n
    #polygon(t,lenght,n,step_angle) 
def arc (t,r,angle):
    arc_circum =(2 * math.pi *r)*abs(angle)/360
    n = int (arc_circum/4)+1
    lenght = arc_circum/n
    step_angle = angle/n
    polygon(t,lenght,n,step_angle)
world = TurtleWorld()
bob =Turtle()
bob.delay = 0.01
square(bob,100)
polygon(bob,100,5,360/5)
circle(bob,75)
arc(bob,150,90)
wait_for_user()

