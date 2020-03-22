Nama = ('Sri Wahyuni')
NIM = ('H061181001')

print(Nama)
print(NIM)

from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A, b, N=21, x=None):
    if x is None:
        x = zeros(len(A[0]))
    D = diag(A)
    R = A-diagflat(D)
    for i in range(N):
        x = (b-dot(R,x))/D
    return x

A = array([[10., -1., 2., 0.],
          [-1., 11., -1., 3.],
          [2., -1., 10., -1.],
          [0., 3., -1., 8.]])
b = array([6., 25, -11, 15])
guess = array([1.0, 1.0, 1.0, 1.0])
sol = jacobi(A, b, N=25, x=guess)
print('A=')
print(A)
print('b=')
print(b)
print('x=')
print(sol)

