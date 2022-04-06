
from Mat import Matrix

def test_vectors():
    v = Matrix([[1,2,3]])
    u = Matrix([1,2,3]) # test conversion to a matrix
    print("v: \n",v, '\n')
    print("u: \n",u, '\n')
    print("v+u: \n",u+v, '\n')
    print("v-u: \n",u-v, '\n')
    print("v*3: \n",v*3,'\n')
    print("u.T: \n",u.transpose(), '\n')
    print("u.norm(): \n",Matrix.norm(u),'\n')
    print("u.dot(v): \n",Matrix.dot(u,v), '\n')

def test_matrix():
    a = Matrix.create_matrix((2,2),1)
    print("a+3:\n",a+3, '\n')
    print("a-3: \n", a-3, '\n')
    print("a*5: \n", a*5, '\n')

    m1 = Matrix([[1,2,3],[6,2,5]])
    m2 = Matrix([[1, 4, 7, 0], [2, 5, 8, 0], [3, 6, 9, 0]])
    print("m1: \n", m1, '\n')
    print("m2: \n", m2, '\n')
    print("m1.matmul(m2): \n", Matrix.matmul(m1,m2), '\n')
    print("m1.T: \n", m1.transpose(), '\n')
    print("m2: \n", m2, '\n')
    m2[1][2] = 99
    print("m2 changed: \n", m2, '\n')


def test_broadcasting():
    v = Matrix([[1,2,3]])
    print("v: \n",v, '\n')
    print("v+5: \n",v+5, '\n')
    print("v-3: \n",v-3, '\n')

def test_copy():
    m1 = Matrix.create_matrix(shape=(3,4),value=1)
    m1_copy = m1.copy()
    print("m1: \n", m1, '\n')
    m1[0][2] = 99
    print("m1: \n", m1, '\n')
    print("m1_copy: \n", m1_copy, '\n')
    print(m1==m1_copy)

def test_argmin():
    v = Matrix([[-4,2,3,5,2,-11,9]])
    print(Matrix.argmin(v))



if __name__=="__main__":
    # test_vectors()
    # test_broadcasting()
    # test_matrix()
    # test_copy()
    test_argmin()