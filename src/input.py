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

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    def myfunc(self):
      print("Hello my name is " + self.name)
      p1 = Person("John", 36)
      p1.myfunc()