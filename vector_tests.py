
from Vector import Vector

def test():
    v = Vector([1,2,3])
    u = Vector([4,5,6])
    r1 = u+v
    r2 = u-v
    r3 = v*3
    r4 = u+10
    r5 = v-1
    r6 = Vector.dot(v,u)
    r7 = Vector.dot(u,v)
    r8 = Vector.m
    r9 = Vector.sqaured_norm(u)

    print(v)
    print(u)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)
    print(r8)
    print(r9)

    r10 = v.copy()
    v[0] = 99
    print(v)
    print(r10)

    w = Vector([0, 0, 0, -1, 0])
    print(w.argmin())

def test_nested():
    a = Vector.create_vector(2,1)
    centers = [[1,2],[3,4]]
    m1 = [Vector(c) for c in centers]
    print(m1)
    for i in range(len(m1)):
        m1[i] += a
    print("after")
    print(m1)





# test()
# test_nested()
a = Vector.create_vector(5,10)
b = Vector.create_vector(5,2)
# print(a)
# print(a/3)
print(a/b)