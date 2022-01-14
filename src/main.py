import sys
while(True):
  print('PLEASE INSERT AN INTEGER NUMBER IN THE RANGE 0-10') 
  
  param1 = input()
  if int(param1) in range(11): 
    while(True):
      print( 'PLEASE INSERT A CHAR PARAMETER IN [A,B,C]')
      param2 = input()
      if param2 in ['A','B','C']:
        print('uso I due parametri passati dall utente: ',param1,param2)
        sys.exit()
      else: 
          print('TRY AGAIN PLEASE')
    else:
     print('TRY AGAIN PLEASE') 

     
def f(y):
  if y >= 0.0:
    return y**5*math.exp(-y)
  else:
    return 0.0
     
infile='mydata.txt'
outfile='myout.txt'
indata = open(infile,'r')
linee=indata.readlines()
indata.close()
processati=[ ]
x=[ ]
for el in linee:
  valori = el.split()
  x.append(float(valori[0])); 
  y = float(valori[1])
  processati.append(f(y))
  outdata = open(outfile, 'w')
  i=0
  for el in processati:
    outdata.write('%g %12.5e\n' % (x[i],el))
    i+=1
    outdata.close()     
  

import numpy as np
input = np.loadtxt('input1.txt', dtype='i', delimiter=',')
print(input)

X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
Y = [[5,8,1,2],[6,7,3,0],[4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# iterate through rows of X
for i in range(len(X)):
  # iterate through columns of Y
  for j in range(len(Y[0])):
    # iterate through rows of Y
    for k in range(len(Y)):
      result[i][j] += X[i][k] * Y[k][j]
      for r in result:
        print(r)