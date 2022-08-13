class oppo:
  def features1(self):
    print("Android OS")

class Iphone:
  def features2(self):
    print("Iphone OS ")

class LG(oppo,Iphone):
  def features3(self):
    print("5G Mobile")

A5 = oppo()
s7 = Iphone()
s10 = LG()

s10.features1()
s10.features2()
s10.features3()
