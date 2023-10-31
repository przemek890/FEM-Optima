import numpy as np
from src.siatka import Grid
from src.Element_uniwersalny import *
""""""""""""""""""""""""
class Matrix_H:
    def __init__(self, points):
        self.points = points
        if self.points == 2:
            # grid = Grid(path)

            # TODO: tymczasowe do testow: ->
            from  src.siatka import Element,Node
            self.k = 30
            vec4 = [Node(0,0),Node(0.025,0),Node(0.025,0.025),Node(0,0.025)]
            vec_4 = Element(vec4)
            # TODO: tymczasowe do testow <-

            vec_el_ksi = dNdksi(2)
            vec_el_eta = dNdeta(2)

            self.matrix_dx = np.zeros((4, 4))
            self.matrix_dy = np.zeros((4, 4))
            for i in range(4):
                for j in range(4):
                    vec_2 = np.array([vec_el_ksi.matrix[i][j],vec_el_eta.matrix[i][j]])
                    wynik = self.przejscie(*gauss_points["p2"][j],vec_2,vec_4)
                    vec_dx_dy = wynik[0]
                    self.jacobian = wynik[1]
                    self.matrix_dx[i][j] = vec_dx_dy[0]
                    self.matrix_dy[i][j] = vec_dx_dy[1]

            self.matrix_dx,self.matrix_dy = self.transposition_multiply()   # Tablica macierzy po przemnożeniu każdego wiersza przez jego transpozycje

            self.H_matrices = []
            for i in range(4):
                H_i = self.k * (self.matrix_dx[i] + self.matrix_dy[i]) * self.jacobian
                self.H_matrices .append(H_i)


        else:
            raise ("Bład liczby puntow")



    @staticmethod
    def przejscie(ksi, eta, vec2, vec4):
        dxdksi = lambda vec4, eta: 0.25 * eta * (vec4[0].x - vec4[1].x + vec4[2].x - vec4[3].x) + 0.25 * (
                    - vec4[0].x + vec4[1].x + vec4[2].x - vec4[3].x)
        dydksi = lambda vec4, eta: 0.25 * eta * (vec4[0].y - vec4[1].y + vec4[2].y - vec4[3].y) + 0.25 * (
                    - vec4[0].y + vec4[1].y + vec4[2].y - vec4[3].y)
        dxdeta = lambda vec4, ksi: 0.25 * ksi * (vec4[0].x - vec4[1].x + vec4[2].x - vec4[3].x) + 0.25 * (
                    - vec4[0].x - vec4[1].x + vec4[2].x + vec4[3].x)
        dydeta = lambda vec4, ksi: 0.25 * ksi * (vec4[0].y - vec4[1].y + vec4[2].y - vec4[3].y) + 0.25 * (
                    - vec4[0].y - vec4[1].y + vec4[2].y + vec4[3].y)

        matrix = np.array([[dxdksi(vec4, eta), dxdeta(vec4, ksi)], [dydksi(vec4, eta), dydeta(vec4, ksi)]])
        determinant = np.linalg.det(matrix)
        reverse_mat = np.array([[dydeta(vec4, ksi), -dxdeta(vec4, ksi)], [-dydksi(vec4, eta), dxdksi(vec4, eta)]])

        wynik = (1. / determinant) * reverse_mat @ vec2

        return wynik, determinant
    def transposition_multiply(self):
        H_matrices_for_points_x = []
        H_matrices_for_points_y = []
        if self.points == 2:
            for i in range(4):
                H_matrix = np.array([self.matrix_dx[:,i]]).T @ [self.matrix_dx[:,i]] # Odwrotnie transpozycja z powodu zapisu w macierzy na odwrót
                H_matrices_for_points_x.append(H_matrix)

            for i in range(4):
                H_matrix = np.array([self.matrix_dy[:,i]]).T @ [self.matrix_dy[:,i]] # Odwrotnie transpozycja z powodu zapisu w macierzy na odwrót
                H_matrices_for_points_y.append(H_matrix)


            return H_matrices_for_points_x,H_matrices_for_points_y

    def Get_H_matrices(self):
        return self.H_matrices

