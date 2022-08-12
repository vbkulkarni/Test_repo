#Add class method & static method
class student:
  institute = 'KT Academy' #Class Variable

  def __init__(self,sql,python,tableau,powerbi):
    self.sql = sql
    self.python = python
    self.tableau = tableau
    self.powerbi = powerbi

  def avg_stud (self): #Instance Method
    return (self.sql + self.python + self.tableau + self.powerbi)/4

  @classmethod #Declaration of class method
  def info(cls):
    return cls.institute
  
  @staticmethod # Declaration of static method
  def getinstitute():
    print("This is student of DA")

 
vivek = student(61,87,77,81)
prasad = student(39,35,31,40)

print(vivek.avg_stud())
print(prasad.avg_stud())


