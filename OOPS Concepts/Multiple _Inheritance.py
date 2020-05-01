class A:
    varA = 10
    def funA(self):
        return 11

class B:
    varB = 20
    def funB(self):
        return 21

class C(A, B):
    varC = 30
    def funC(self):
        return 31

obj = C()
print(obj.varA, obj.funA(), sep="\t")
print(obj.varB, obj.funB(), sep="\t")
print(obj.varC, obj.funC(), sep="\t")

# Important Notes

# 1. If Class B and C have the same variable name (for ex: var), the value defined in Class B is overridden by class C
# 2. Python uses "Bottom Up Approach" to read the entities.
# 3, When 2 superclasses have the same names for entities and if python cannot deduce the inherance path: the precedence is taken from Left --> Right (In the example above: First class 'A' followed by 'B') 