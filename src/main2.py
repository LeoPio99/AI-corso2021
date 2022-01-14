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