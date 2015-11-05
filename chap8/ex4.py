def rotate(word,num):
  n = 0
  s = "" 
  l ='abcdefghijklmnopqrstuvwxyz'
  for i in word:
    for j in range(len(l)):
       if i == l[j]:
          n = j+num
    s = s+l[n]
  return s
print rotate('cheer',7)
