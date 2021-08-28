class base_class:
    def insert_name(self,name):
        self.name=name
    def __add__(self, other):
        name=self.name+other.name
        return name

x=base_class()
y=base_class()

x.insert_name("hilal")
y.insert_name("yui")

fullname=x+y
print(fullname)