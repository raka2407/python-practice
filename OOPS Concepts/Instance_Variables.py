class ExampleClass:
    def __init__(self, val=1):
        self.__first = val

    def setSecond(self, val):
        self.__second = val

eobject1 = ExampleClass(10)  # eobject1 has only 1 property named first

eobject2 = ExampleClass()
eobject2.setSecond(2)        # eobject2 has 2 properties: named first and second

eobject3 = ExampleClass(20)
eobject3.setSecond(30)
eobject3.third = 30          # eobject3 has 3 properties: named first, second and third. 

print(eobject1.__dict__)
print(eobject2.__dict__)
print(eobject3.__dict__)

# prints the following content

#    {'_ExampleClass__first': 10}
#    {'_ExampleClass__first': 1, '_ExampleClass__second': 2}
#    {'_ExampleClass__first': 20, '_ExampleClass__second': 30, 'third': 30}

eobject3.__fourth = 40   # __ can be given to variable names to make them private

#Each of these variables can be directly accessed outside the class using objectname._ClassName__variableName. Please see below
print(eobject1._ExampleClass__first)
print(eobject3._ExampleClass__fourth)  # throws and error as this instance variable is defined outside the class code.
