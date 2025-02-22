import numpy as np


class Aggregation:
    def __init__(self,grid,global_data):
        self.grid = grid
        self.global_data = global_data
        self.dim = dim = int(global_data["Nodes_number"])

        self.global_H = np.zeros((dim,dim))
        self.where_ids_H = []

        self.global_C = np.zeros((dim,dim))
        self.where_ids_C = []

        self.global_P = np.zeros((dim,1))
        self.where_ids_P = []

        ################################################### Macierz_H_global
        for element in grid.elements:
            where_ids = np.empty((4, 4), dtype=object)
            for i, id1 in enumerate(element.nodes_IDs):
                for j, id2 in enumerate(element.nodes_IDs):
                    where_ids[i][j] = (id1, id2)
            self.where_ids_H.append(where_ids)
        self.fill_matrix_H()
        ################################################### Macierz_C
        for element in grid.elements:
            where_ids = np.empty((4, 4), dtype=object)
            for i, id1 in enumerate(element.nodes_IDs):
                for j, id2 in enumerate(element.nodes_IDs):
                    where_ids[i][j] = (id1, id2)
            self.where_ids_C.append(where_ids)
        self.fill_matrix_C()
        ################################################### Vector_P_global
        for element in grid.elements:
            where_ids = np.zeros((1, 4),dtype=int)
            for i, id in enumerate(element.nodes_IDs):
                where_ids[0][i] = int(id)
            self.where_ids_P.append(where_ids)
        self.fill_vector_P()


    def fill_matrix_H(self):
        for element, id_mat in zip(self.grid.elements, self.where_ids_H) :
            H = element.matrix_H
            HBC = element.matrix_HBC
            for i in range(4):
                for j in range(4):
                    x,y = id_mat[i][j]
                    self.global_H[x][y] += H[i][j]
                    self.global_H[x][y] += HBC[i][j]
    def fill_matrix_C(self):
        for element, id_mat in zip(self.grid.elements, self.where_ids_C) :
            C = element.matrix_C
            for i in range(4):
                for j in range(4):
                    x,y = id_mat[i][j]
                    self.global_C[x][y] += C[i][j]
    def fill_vector_P(self):
        for element, id_vec in zip(self.grid.elements, self.where_ids_P):
            P = element.vectorP
            for i in range(4):
                x = id_vec[0][i]
                self.global_P[x][0] += P[i]
        # np.set_printoptions(edgeitems=16, linewidth=100000)
        # print(self.global_P)


    def test_H_global(self):
        print("\033[91m" + "______________________________MatrixH______________________________" + "\033[0m")
        np.set_printoptions(edgeitems=16, linewidth=100000)
        print(self.global_H)
        print("\033[91m" + "___________________________________________________________________" + "\033[0m")
    def test_P_global(self):
        print("\033[94m" + "______________________________VectorP______________________________" + "\033[0m")
        np.set_printoptions(edgeitems=16, linewidth=100000)
        print(self.global_P)
        print("\033[94m" + "___________________________________________________________________" + "\033[0m")
    def test_C_global(self):
        print("\033[95m" + "______________________________MatrixC______________________________" + "\033[0m")
        np.set_printoptions(edgeitems=16, linewidth=100000)
        print(self.global_C)
        print("\033[95m" + "___________________________________________________________________" + "\033[0m")

    ######################################## Solve:















