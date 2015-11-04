def check_trangle(a,b,c):
   if a+b < c or a+c < b or b+c < a:
      print 'can\'t make trangle on this lenght'
   else:
      print'yes,we will make a triangle on this length'
h =int(raw_input('>>'))
s1 =int(raw_input('>>'))
s2 = int(raw_input('>>'))
n =check_trangle(h,s1,s2)
