from src.siatka import Grid, Global_Data, Element, Node
from src.Element_uniwersalny import *
from data.Gauss_points import gauss_weights
""""""""""""""""""""""""
class Matrix_H:
    def __init__(self,points,path):
        self.points = points
        if self.points == 2:
            vec_el_ksi = dNdksi(2)
            vec_el_eta = dNdeta(2)
        elif self.points == 3:
            vec_el_ksi = dNdksi(3)
            vec_el_eta = dNdeta(3)
        elif self.points == 4:
            vec_el_ksi = dNdksi(4)
            vec_el_eta = dNdeta(4)
        else:
            raise ("Bład liczby puntow")

        global_data = Global_Data(path)
        grid = Grid(path)
        self.k = global_data["Conductivity"]

        self.H_matrices = []    # Lista macierzy H dla wszystkich elementów vec4
        for vec_4 in grid.elements:
            H_matrix = self.generate_H_matrix_for_element(vec_el_ksi,vec_el_eta,vec_4)
            self.H_matrices.append(H_matrix)


    def generate_H_matrix_for_element(self,vec_el_ksi,vec_el_eta,vec_4):
        self.matrix_dx = np.zeros((self.points ** 2, 4))
        self.matrix_dy = np.zeros((self.points ** 2, 4))
        list_jacobian = []
        for i in range(self.points ** 2):
            for j in range(4):
                vec_2 = np.array([[vec_el_ksi.matrix[i,j], vec_el_eta.matrix[i,j]]])
                vec_dNidksi = np.array(vec_el_ksi.matrix[i,:])
                vec_dNideta = np.array(vec_el_eta.matrix[i,:])
                wynik = self.przejscie(vec_dNidksi,vec_dNideta,vec_2, vec_4)
                vec_dx_dy = wynik[0]
                jacobian = wynik[1]
                self.matrix_dx[i][j] = vec_dx_dy[0]
                self.matrix_dy[i][j] = vec_dx_dy[1]
            list_jacobian.append(jacobian)

        self.matrix_dx, self.matrix_dy = self.transposition_multiply()  # Tablica macierzy po przemnożeniu każdego wiersza przez jego transpozycje


        self.H_matrix = []  # Tablica poszczególnych macierzy cząstkowych - macierzy H
        for i in range(self.points ** 2):
            H_i = self.k * (self.matrix_dx[i] + self.matrix_dy[i]) * list_jacobian[i]
            self.H_matrix.append(H_i)

        if self.points == 2:
            for i, w in enumerate(gauss_weights["w2"]):
                self.H_matrix[i] *= w[0] * w[1]
        elif self.points == 3:
            for i, w in enumerate(gauss_weights["w3"]):
                self.H_matrix[i] *= w[0] * w[1]
        elif self.points == 4:
            for i, w in enumerate(gauss_weights["w4"]):
                self.H_matrix[i] *= w[0] * w[1]
        else:
            raise ("Bład liczby puntow")

        self.H_matrix = np.sum(self.H_matrix,axis=0)
        return self.H_matrix
    @staticmethod
    def przejscie(vec_dNidksi,vec_dNideta,vec2,vec4):
        dxdksi = vec_dNidksi[0] * vec4[0].x + vec_dNidksi[1] * vec4[1].x + vec_dNidksi[2] * vec4[2].x + vec_dNidksi[3] * vec4[3].x
        dydksi = vec_dNidksi[0] * vec4[0].y + vec_dNidksi[1] * vec4[1].y + vec_dNidksi[2] * vec4[2].y + vec_dNidksi[3] * vec4[3].y
        dxdeta = vec_dNideta[0] * vec4[0].x + vec_dNideta[1] * vec4[1].x + vec_dNideta[2] * vec4[2].x + vec_dNideta[3] * vec4[3].x
        dydeta = vec_dNideta[0] * vec4[0].y + vec_dNideta[1] * vec4[1].y + vec_dNideta[2] * vec4[2].y + vec_dNideta[3] * vec4[3].y

        matrix = np.array([[dxdksi,dydksi],
                           [dxdeta, dydeta]])

        determinant = np.linalg.det(matrix)
        reverse_mat = np.array([[dydeta,-dydksi],
                                [-dxdeta , dxdksi]])

        wynik = (1. / determinant) * reverse_mat @ vec2.T

        return wynik, determinant
    def transposition_multiply(self):
        H_matrices_for_points_x = []
        H_matrices_for_points_y = []
        for i in range(self.points ** 2):
            H_matrix = np.array([self.matrix_dx[i,:]]).T @ [self.matrix_dx[i,:]] # Odwrotnie transpozycja z powodu zapisu w macierzy na odwrót
            H_matrices_for_points_x.append(H_matrix)

        for i in range(self.points ** 2):
            H_matrix = np.array([self.matrix_dy[i,:]]).T @ [self.matrix_dy[i,:]] # Odwrotnie transpozycja z powodu zapisu w macierzy na odwrót
            H_matrices_for_points_y.append(H_matrix)

        return H_matrices_for_points_x,H_matrices_for_points_y


    def get_H_matrices(self):
        return self.H_matrices

