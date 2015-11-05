def palindrome(word):
   s = ""
   for i in word[::-1]:
     s = s+i
   
   if s ==word:
     return True
   else:
     return False
print palindrome('limil')
