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