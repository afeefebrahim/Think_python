def count (string,letter):
   c = 0
   for i in string:
      if i == letter:
          c=c+1
   return c
s ='how many e letters are in this string'
print count(s,'i') 
