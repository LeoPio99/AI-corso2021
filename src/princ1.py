import scipy.optimize
import numpy as np
np.info(scipy.optimize.fmin)
np.info(scipy.optimize)
from scipy import fftpack
b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum " ,b,"+",c, "= ", b+c)
b+=1
print("Autoincrement b +=1 b=", b)
print("Multiply c*3 " ,c, "* 3= ",c*3)
print("Sin (c)", np.sin(c))
