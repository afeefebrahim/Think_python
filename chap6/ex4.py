#The Ackermann function, A(m, n), is defined:
def acker(m,n):
   if m == 0:
     n = n+1
     print n
   if m > 0 and n ==0:
     m =m-1
     print 'A(%d,1)'%m
   if m > 0 and n > 0:
     r = m-1
     n = n-1
     print 'A(%d,A(%d,%d))'%(r,m,n)
s = acker(5,3)

