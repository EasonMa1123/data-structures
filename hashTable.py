class hashTable:
  
  def __init__(self,size):
    self.__table =[[] for _ in range(size)]
    self.__size = size


  def __hash(self,value):
    return (value+10) % self.__size



  def addValue(self,value):
    hashed_value = self.__hash(value if type(value) == int else sum(ord(i) for i in value))
    if value in self.__table[hashed_value]:
      return
    else:
      self.__table[hashed_value].append(value)
    

  def __str__(self):
    return str(self.__table)
  
  def cotain (self,value):
    hashed_value = self.__hash(value if type(value) == int else sum(ord(i) for i in value) )
    if value in self.__table[hashed_value]:
      return True
    else:
      return False 
