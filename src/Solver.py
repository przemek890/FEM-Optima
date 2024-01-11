import numpy as np
from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix


class Solver:
    def __init__(self,global_data,global_H,global_P,global_C):
        self.global_H = global_H
        self.global_P = global_P
        self.global_C = global_C
        self.global_data = global_data

        self.SimulationTime = global_data["SimulationTime"]
        self.SimulationStepTime = global_data["SimulationStepTime"]
        self.InitialTemp = global_data["InitialTemp"]

        self.T0 = np.full((self.global_data["Nodes_number"],1), self.InitialTemp)

    def print_T(self,T,time):
        print("\033[92m" + f"______________________________VectorT // time={time}______________________________" + "\033[0m")
        T_array = np.array(T)
        np.set_printoptions(self.global_data["Nodes_number"], linewidth=100000)
        print(T_array.reshape(1,-1))
        print("min: ",min(T_array),"; max:",max(T_array))
        print("\033[92m" + "__________________________________________________________________________________" + "\033[0m")

    ######################################## Solve:
    def solve(self):
        matric_c_per_step = self.global_C / self.SimulationStepTime
        matrix_glob = self.global_H + matric_c_per_step

        T_opt = []

        for time in range(self.SimulationStepTime,self.SimulationTime + self.SimulationStepTime,self.SimulationStepTime):
            T1 = spsolve(csr_matrix(matrix_glob), self.global_P + (matric_c_per_step @ self.T0))

            T1 = np.array(T1).reshape(-1,1)

            self.print_T(T1,time)
            T_opt.append(T1)
            self.T0 = T1

        return np.array(T_opt)








