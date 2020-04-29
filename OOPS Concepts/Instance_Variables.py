class ExampleClass:
    def __init__(self, val=1):
        self.__first = val

    def setSecond(self, val):
        self.__second = val

eobject1 = ExampleClass(10)
eobject1.setSecond(20)

eobject2 = ExampleClass()
eobject2.setSecond(2)

print(eobject1.__dict__)
print(eobject2.__dict__)