The built-in function eval takes a string and evaluates it using the Python interpreter. For example:
def eval_loop(string): 
    r = eval(string)
    if string == 'done':
      print r
     
    print 'enter the expersion if you complete then enter done'
    exp = raw_input('>>') 
    p = eval_loop(exp)   
   
n = eval_loop ('1+2+3+4')
