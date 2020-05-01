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