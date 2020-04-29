class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
    

class AddStack(Stack):         # Inherite from Super Class
    def __init__(self):
        Stack.__init__(self)   # Initialization of Super Class
        self.__sum = 0

    def push(self, val):       # Orerride Super Class Method
        Stack.push(self, val)  
        self.__sum += val

    def pop(self):              # Orerride Super Class Method
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def getSum(self):
        return self.__sum

as1 = AddStack()
as2 = AddStack()
as1.push(5)
as1.push(10)
as1.push(25)
as2.push(as1.pop())  # pop - LIFO Last In First Out Operation
print(as2.pop())
print(as1.getSum())