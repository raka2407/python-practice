class A:
    pass

class B(A):     # B inherited from A
    pass

class C(B):     # C inherited from B
    pass

for cls1 in [A, B, C]:
    for cls2 in [A, B, C]:
        print(issubclass(cls1, cls2), end="\t")
    print()