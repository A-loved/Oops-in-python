class Mybaseclass:
    def set_name(self,name):
        self.name = name

class subclass(Mybaseclass):
    def display(self):
        print("name is :" +str(self.name))


y = subclass()
y.set_name("akshay")
y.display()
