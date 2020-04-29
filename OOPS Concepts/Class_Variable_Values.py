class Example:
    varia = 1
    def __init__(self, val):
        varia = val
    
print(Example.varia)
exampleObject = Example(2)
print(exampleObject.varia) 

# Following is the output based on how varia is referenced in the init method.

# Case: self.varia = val 
# output:  1 
#          2

# Case: Example.varia = val 
# output:  1 
#          2

# Case: varia = val 
# output:  1 
#          1