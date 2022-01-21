import scipy.optimize
import numpy as np
b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum " ,b,"+",c, "= ", b+c)
b+=1
print("Autoincrement b +=1 b=", b)
print("Multiply c*3 " ,c, "* 3= ",c*3)
print("Sin (c)", np.sin(c))

g=np.arange(1,5)
h=np.array([[1,1,1,1],[2,2,2,2]])
print(h+g)

v1=np.array([1,2,3])
v2=np.array([10,20,30])
print(v1*v2)
print(np.dot(v1,v2))

a=np.arange(25)
a=a.reshape((5,5)) 
print(a)

a=np.arange(5)
a: [0,1,2,3,4]
b=a
b[0]=100
print ("a:", a , "b:" , b)

x=np.arange(1,5)
def func_NumPy(x):
 r = x.copy() #allocate result array
 for i in range(np.size(x)):
  if x[i] < 0:
   r[i] = 0.0
  else:
   r[i] = sin(x[i])
 return r

