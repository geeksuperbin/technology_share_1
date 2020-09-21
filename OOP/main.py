from people import People
from dog import Dog
from cat import Cat


a =  People('男')
a.call()
a.say_sex()

print("----------------")

b =  People('女')
b.call()
b.say_sex()

print("----------------")

c = Dog()
c.call()

print("----------------")

c = Cat()
c.call()