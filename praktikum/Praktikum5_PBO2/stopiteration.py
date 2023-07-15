class printNum:
  def __iter__(self):
    self.z = 2
    return self

  def __next__(self):
    if self.z <= 20:   #performing the action like printing the value on console till the value reaches 20
      y = self.z
      self.z += 2
      return y
    else:
      raise StopIteration   #raising the StopIteration exception once the value gets              increased from 20

obj = printNum()
value_passed = iter(obj)

for u in value_passed:
  print(u)