
class Person:
  def __init__(self, name):
    self.name = name

  def talk(self):
    print(f'hi, I am {self.name}')


john = Person('Harry Kaela')
john.talk()

bob = Person("Bob  Marley")
bob.talk()