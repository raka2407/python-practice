class A:
    pass

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()

for ob in [a, b, c]:
    for cls in [A, B, C]:
        print(isinstance(ob, cls), end="\t")
    print()