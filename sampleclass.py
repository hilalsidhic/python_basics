# class Mysampleclass:
#     def hello(self,name):
#         self.test=name
#     def printh(self):
#         print(self.test)
#
# x=Mysampleclass()
# y=Mysampleclass()
# name="muhammed hilal"
# x.hello(name)
# y.hello("siyauiu")
#
# x.printh()
# y.printh()

class userDetails:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def addage(self):
        self.age=self.age+1
    def changeName(self,name):
        self.name=name
    def printdetails(self):
        print("Name:"+self.name)
        print("Age:"+str(self.age))

    #@classmethod
    #@staticmethod

x=userDetails(input("enter first name and age:"),int(input()))
y=userDetails(input("enter second name and age"),int(input()))

x.addage()
y.changeName("hilal")

x.printdetails()
y.printdetails()

# class Mysampleclass:
#     def __init__(self,name,age,place):
#         print("hello"+name+str(age)+place)
#
# x=Mysampleclass("hilal",12,"dsafsdf")
# y=Mysampleclass("hsdfas",32,"ttyt")