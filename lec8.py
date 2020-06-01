"""
Lecture 8
"""

#def my_function(a,b = 0):
     
  #  print('a is', a)
 #   print('b is', b)
  #  return a + b    # return is always the last step of the function 
    
#print(my_function(a=1))

#ex1
#def calculate_abs(a):
   # if type(a) is str:
   #     return ('wrong data type')
   # if a >0:
   #     return a
    #if a <0:
   #     return -a
#print(calculate_abs('a'))

#ex2

#def calc_sigma(m,n):
    
 #   result = 0
 #   for i in range(n,m +1):
  #      result = result + i
   # return result 

#print(calc_sigma(5,3))

#def calc_pi(m,n):
    
 #   result = 1
 #   for i in range(n,m +1):
#        result = result * i
 #   return result 

#print(calc_pi(5,3))

#ex3
#def calc_f(m):
#    if m ==0:
 #       return 1
  #  else:
   #     return m * calc_f(m-1)
#print(calc_f(3))

#def cal_p(m,n):
 #   return cal_f(m)/cal_f(m-n)
#print(cal_p(5,3))