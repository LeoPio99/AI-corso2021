a=300
b=2.1
print(a+b)
c=20-4.2j
print(c.real)
print(c.imag)
print(a==b)
print(a>b)
import math
print(math.pi)
print(math.cos(1))
h='hello'
print(h+h)
print(h[1:4])
k='ciao\tciao'
print(k)

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

number = 23
guess=int(input('Enter an integer : '))
if guess == number:
  # New block starts hereprint('Congratulations, you guessed it.')
   print('Congratulations, you guessed it(but you do not win any prizes!)')
  # New block ends here
elif guess < number:
    # Another block
     print('No, it is a little higher than that')
else:
       print('No, it is a little lower than that')# you must have guessed > number to reach here
 
number = 23
running = True
while running:
  guess = int(input('Enter an integer : '))
  if guess == number:
    print('Congratulations, you guessed it.')
    # this causes the while loop to stop
    running = False
  elif guess < number:
      print('No, it is a little higher than that.')
  else:
        print('No, it is a little lower than that.')

a=[1,2,3,4,5]
for el in a:
   print(el)
