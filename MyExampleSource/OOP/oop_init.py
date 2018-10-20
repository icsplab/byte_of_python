class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print 'Hello, I`m', self.name

p = Person("Jawth")
p.say_hi()