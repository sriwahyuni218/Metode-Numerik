Nama = ('Sri Wahyuni')
NIM = ('H061181001')

print(Nama)
print(NIM)

import numpy as np
A= np.array([[3., -0.1, -0.2, 7.85],
             [0.1,7., -0.3, -19.3],
             [0.3, -0.2, 10, 71.4]])
m = A[1,0]/A[0,0]
A[1,0]=A[1,0]-m*A[0,0]
A[1,1]=A[1,1]-m*A[0,1]
A[1,2]=A[1,2]-m*A[0,2]
A[1,3]=A[1,3]-m*A[0,3]

print(A)
