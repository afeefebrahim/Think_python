#Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
#an + bn = cn 
#for any values of n greater than 2.
def fermat(a,b,c,n):
   if n <= 2:
      if a**n+b**n == c**n:
          print "holy smokes,fermat was wrong!"
      else:
          print "no that is not working"
   else:
       print "the number is less than 2 is not applicable" 
n =fermat(3,4,5,2)
 
