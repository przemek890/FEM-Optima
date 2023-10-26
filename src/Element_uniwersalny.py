import numpy as np
from data.Gauss_points import gauss_points
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class dNdksi:
    N1dksi = lambda eta,ksi: -0.25 * (1 - ksi)
    N2dksi = lambda eta,ksi: 0.25 * (1 - ksi)
    N3dksi = lambda eta,ksi: 0.25 * (1 + ksi)
    N4dksi = lambda eta,ksi: -0.25 * (1 + ksi)
    funkcje = [N1dksi,N2dksi,N3dksi,N4dksi]

    def __init__(self, points):
        if points == 2:
            self.matrix = np.zeros((4, 4))
            for i in range(4):
                for j in range(4):
                    self.matrix[i][j] = self.funkcje[i](*gauss_points["p2"][j])

        elif points == 3:
            self.matrix = np.zeros((4, 9))
            for i in range(4):
                for j in range(9):
                    self.matrix[i][j] = self.funkcje[i](*gauss_points["p3"][j])
        elif points == 4:
            self.matrix = np.zeros((4, 16))
            for i in range(4):
                for j in range(16):
                    self.matrix[i][j] = self.funkcje[i](*gauss_points["p4"][j])

        else: raise("Bład liczby puntow")


    def matrix(self):
        return self.matrix
class dNdeta:
    N1dksi = lambda eta, ksi: -0.25 * (1 - eta)
    N2dksi = lambda eta, ksi: -0.25 * (1 + eta)
    N3dksi = lambda eta, ksi: 0.25 * (1 + eta)
    N4dksi = lambda eta, ksi: 0.25 * (1 - eta)
    funkcje = [N1dksi, N2dksi, N3dksi, N4dksi]

    def __init__(self, points):
        if points == 2:
            self.matrix = np.zeros((4, 4))
            for i in range(4):
                for j in range(4):
                    self.matrix[i][j] = self.funkcje[i](*gauss_points["p2"][j])

        elif points == 3:
            self.matrix = np.zeros((4, 9))
            for i in range(4):
                for j in range(9):
                    self.matrix[i][j] = self.funkcje[i](*gauss_points["p3"][j])
        elif points == 4:
            self.matrix = np.zeros((4, 16))
            for i in range(4):
                for j in range(16):
                    self.matrix[i][j] = self.funkcje[i](*gauss_points["p4"][j])

        else:
            raise ("Bład liczby puntow")
