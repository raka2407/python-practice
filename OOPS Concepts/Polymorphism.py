class A:
    def doit(self):
        print("Printing from A")

    def doanything(self):
        self.doit()

class B(A):
    def doit(self):
        print("Printing from B")

obj1 = A()
obj2 = B()

obj1.doanything()
obj2.doanything()  #Overrides the method in Class 'A'

#Important Notes#
1. One of the main advantages of polymorphism is to define the abstract method in super class and override its functionality in subclasses that inherite the super class.
