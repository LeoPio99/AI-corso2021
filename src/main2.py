m=[1,3,'list']
print(m[0],m[2])
print(3 in m)
a=range(1,15)
b=range(1,9)
print(a[2])
c=[e1-e2 for e1 in a for e2 in b]
print(c)

import time
l=list(range(10000000))
v=list(range(1000000))
T1=time.perf_counter()
s=l+v
T2=time.perf_counter()
print( '+ execution time:' , T2-T1, 's')
T3=time.perf_counter()
l.extend(v)
T4=time.perf_counter()
print('extend execution time:', T4-T3 , 's')

beppe=list(range(5))
print('Initial beppe: ', beppe)
for i in list(range(5,7)):
   beppe.append(i)
print ('Append: ', beppe)
beppe.pop()
print ('Pop: ', beppe)

tup1=(1,2,3,4)
'tup1[3]=0'

d={}
print(d)
my_dict={'nome': 'Leonardo', 'cognome': 'Piovan'}
print(my_dict['nome'])
