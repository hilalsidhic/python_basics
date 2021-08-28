class baseclass:
    def displey(self):
        print("hello")

class subclass(baseclass):
    def welcome(self):
        print("welcome")

x=baseclass()
x.displey()

y=subclass()
y.displey()
y.welcome()

#super() to access function of base class from sub class
#multiple inheriteence sample

class first:
    def display(self):
        print("first")
class second:
    def display(self):
        print("second")
class third(second,first):
    def displaythird(self):
        print("third")
print("---------------------------------")
x=third()
x.display()
x.displaythird()
print(third.mro())
