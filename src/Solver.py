import numpy as np

class Solver:
    def __init__(self,global_H,global_P):
        self.global_H = global_H
        self.global_P = global_P
    ######################################## Solve:
    def solve(self):
        from scipy.sparse.linalg import spsolve
        from scipy.sparse import csr_matrix
        H_csr = csr_matrix(self.global_H)

        T = spsolve(H_csr, -self.global_P)

        print("\033[92m" + "______________________________VectorT______________________________" + "\033[0m")
        T_array = np.array(T)
        T_matrix = T_array.reshape((-1, 1))
        print(T_matrix)
        print("\033[92m" + "___________________________________________________________________" + "\033[0m")


