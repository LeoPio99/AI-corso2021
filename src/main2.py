class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

import sys
for arg in sys.argv[1:]:
  try:
    f = open(arg, 'r')
  except OSError:
      print('cannot open', arg)
  else:
      print(arg, 'has', len(f.readlines()), 'lines')
      f.close()      

x = range(3, 20, 2)
for n in x:
  print(n)

a = ("Marco", "Luca", "Claudio")
b = ("Giovanna", "Maria", "Anna", "Francesca")
z = zip(a, b) 
print(tuple(z))

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)
print(result_list)
c, v =  zip(*result_list)
print('c =', c)
print('v =', v)