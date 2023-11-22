class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    if self._value[-1] == ".":
      return True
    else:
      return False
  
  def is_question(self):
    if self._value[-1] == "?":
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self._value[-1] == "!":
      return True
    else:
      return False
    
  # def count_sentences(self):
  #   count = 0
  #   li = [".", "!", "?"]
  #   for v in self._value:
  #     if len(self._value) > self._value.index(v)+1:
  #       if v in li and self._value[self._value.index(v)+1] == " ":
  #         count += 1
  #   if self._value[-1] in li:
  #       count +=1
  #   return count

  def count_sentences(self):
    count = 0
    string2 = self._value.replace("?", ".")
    string3 = string2.replace("!", ".")
    res = string3.split(".")
    for st in res:
      if st:
        count +=1
    return count