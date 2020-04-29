class ExampleClass:
    counter = 0
    def __init__(self,val):
        self.val = val
        ExampleClass.counter += 1
    
ecobject1 = ExampleClass(10)
ecobject2 = ExampleClass(20)
ecobject3 = ExampleClass(30)

print(ecobject1.__dict__, ExampleClass.counter)
print(ecobject2.__dict__, ExampleClass.counter)
print(ecobject3.__dict__, ExampleClass.counter)

# Outputs the following #

#    {'val': 10} 3
#    {'val': 20} 3
#    {'val': 30} 3

# Important Notes
# 1. Class variables are not shown in object's __dict__
# 2. Class variables have the same value for all the class instances(objects). 
