#A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f):
  print f
  print f
def print_spam():
  return 'spam'
 # n = do_twice(print_spam())
r =do_twice(print_spam())
