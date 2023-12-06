from src.siatka import Grid, Global_Data, Element, Node
from src.Element_uniwersalny import *
from data.Gauss_points import gauss_weights
""""""""""""""""""""""""
class Matrix_C:
    def __init__(self,points,path):
        self.points = points
        if self.points == 2:
            vec_el_ksi = dNdksi(2)
            vec_el_eta = dNdeta(2)
            self.vec_el_N = NFun(2)

        elif self.points == 3:
            vec_el_ksi = dNdksi(3)
            vec_el_eta = dNdeta(3)
            self.vec_el_N = NFun(3)

        elif self.points == 4:
            vec_el_ksi = dNdksi(4)
            vec_el_eta = dNdeta(4)
            self.vec_el_N = NFun(4)
        else:
            raise ("Bład liczby puntow")

        global_data = Global_Data(path)
        grid = Grid(path)
        self.cp = global_data["SpecificHeat"]
        self.rho = global_data["Density"]

        self.C_matrices = []    # Lista macierzy C dla wszystkich elementów vec4
        for vec_4 in grid.elements:
            C_matrix = self.generate_C_matrix_for_element(vec_el_ksi,vec_el_eta,vec_4)
            self.C_matrices.append(C_matrix)

    def generate_C_matrix_for_element(self,vec_el_ksi,vec_el_eta,vec_4):
        self.matrix_dx = np.zeros((self.points ** 2, 4))
        self.matrix_dy = np.zeros((self.points ** 2, 4))
        list_jacobian = []
        for i in range(self.points ** 2):
            for j in range(4):
                vec_dNidksi = np.array(vec_el_ksi.matrix[i,:])
                vec_dNideta = np.array(vec_el_eta.matrix[i,:])
                wynik = self.jacobian_calculate(vec_dNidksi,vec_dNideta, vec_4)
                jacobian = wynik
            list_jacobian.append(jacobian)

        self.matrix_N = self.transposition_multiply()  # Tablica macierzy po przemnożeniu każdego wiersza przez jego transpozycje

        self.C_matrix = []  # Tablica poszczególnych macierzy cząstkowych - macierzy C
        for i in range(self.points ** 2):
            Cpci = self.cp * self.rho * self.matrix_N[i] * list_jacobian[i]
            self.C_matrix.append(Cpci)

        if self.points == 2:
            for i, w in enumerate(gauss_weights["w2"]):
                self.C_matrix[i] *= w[0] * w[1]
        elif self.points == 3:
            for i, w in enumerate(gauss_weights["w3"]):
                self.C_matrix[i] *= w[0] * w[1]
        elif self.points == 4:
            for i, w in enumerate(gauss_weights["w4"]):
                self.C_matrix[i] *= w[0] * w[1]
        else:
            raise ("Bład liczby puntow")

        self.C_matrix = np.sum(self.C_matrix,axis=0)
        return self.C_matrix

    @staticmethod
    def jacobian_calculate(vec_dNidksi,vec_dNideta,vec4):
        dxdksi = vec_dNidksi[0] * vec4[0].x + vec_dNidksi[1] * vec4[1].x + vec_dNidksi[2] * vec4[2].x + vec_dNidksi[3] * vec4[3].x
        dydksi = vec_dNidksi[0] * vec4[0].y + vec_dNidksi[1] * vec4[1].y + vec_dNidksi[2] * vec4[2].y + vec_dNidksi[3] * vec4[3].y
        dxdeta = vec_dNideta[0] * vec4[0].x + vec_dNideta[1] * vec4[1].x + vec_dNideta[2] * vec4[2].x + vec_dNideta[3] * vec4[3].x
        dydeta = vec_dNideta[0] * vec4[0].y + vec_dNideta[1] * vec4[1].y + vec_dNideta[2] * vec4[2].y + vec_dNideta[3] * vec4[3].y

        matrix = np.array([[dxdksi,dydksi],
                           [dxdeta, dydeta]])

        determinant = np.linalg.det(matrix)

        return determinant
    def transposition_multiply(self):
        C_matrices = []
        for i in range(self.points ** 2):
            C_matrix = np.array([self.vec_el_N.matrix[i,:]]).T @ [self.vec_el_N.matrix[i,:]] # Odwrotnie transpozycja z powodu zapisu w macierzy na odwrót
            C_matrices.append(C_matrix)
        return C_matrices
    def get_C_matrices(self):
        return self.C_matrices

