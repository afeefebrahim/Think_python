from swampy.TurtleWorld import*
import math
world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01
r = 25
circum = 2*math.pi*r*.5
n =int(circum/4)+1
step_lenght = circum/n
step_angle = 180/n
rt(bob,45)
for j in range(6):
   for i in range(n):
      fd(bob,step_lenght)
      rt(bob,step_angle)
   rt(bob,90)

wait_for_user()
