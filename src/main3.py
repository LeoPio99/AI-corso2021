import numpy as np
input = np.loadtxt('input1.txt', dtype='i', delimiter=',')
print(input)







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