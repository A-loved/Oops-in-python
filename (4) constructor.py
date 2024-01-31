#build a constructor in order to set persons info and display it and then after one year print the age +1 year
#  also you should use a class variable in it and static method.
class Merckemployees:
    year = 2024
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place


    def relocate(self,place):
        self.place = place


    def add_age(self):
        self.age = self.age+1


    def display(self):
        print("year:"+str(Merckemployees.year))
        print("name:"+self.name)
        print("age:"+str(self.age))
        print("place:"+str(self.place))


    @classmethod
    def add_year(cls):
        cls.year = cls.year+1

    @staticmethod
    def print_welcome():
        print("welcome")


Merckemployees.print_welcome()
x = Merckemployees("akshay", 22, "palakkad")
y = Merckemployees("Regi", 52, "palakkad")
x.display()
y.display()
print("---------------------------------")
x.add_age()
y.add_age()
Merckemployees.add_year()
x.display()
y.display()
print("---------------------------------")
x.relocate("bangalore")
y.relocate("bangalore")
x.display()
y.display()




