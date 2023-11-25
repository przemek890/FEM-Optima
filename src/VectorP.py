import numpy as np
from data.Gauss_points import edges_2,edges_3,edges_4, gauss

class VectorP:
    def __init__(self,points,grid,global_data):
        self.points = points
        self.global_data = global_data
        self.grid = grid
        self.alfa = self.global_data["Alfa"]
        self.tot = self.global_data["Tot"]
        self.VectorPs = []  # Lista macierzy HBC dla wszystkich elementów vec4

        if self.points == 2:
            for vec_4 in self.grid.elements:
                self.VectorPs.append(*self.generate_VectorP_for_element(edges_2,vec_4))
        elif self.points == 3:
            for vec_4 in self.grid.elements:
                self.VectorPs.append(*self.generate_VectorP_for_element(edges_3, vec_4))
        elif self.points == 4:
            for vec_4 in self.grid.elements:
                self.VectorPs.append(*self.generate_VectorP_for_element(edges_4, vec_4))
        else:
            raise ("Bład liczby puntow")
    def generate_VectorP_for_element(self,edges,vec_4):
        N1 = lambda ksi, eta: 0.25 * (1 - ksi) * (1 - eta)
        N2 = lambda ksi, eta: 0.25 * (1 + ksi) * (1 - eta)
        N3 = lambda ksi, eta: 0.25 * (1 + ksi) * (1 + eta)
        N4 = lambda ksi, eta: 0.25 * (1 - ksi) * (1 + eta)
        N = [N1,N2,N3,N4]
        edges_list = [edges["edge_d"],edges["edge_r"],edges["edge_t"],edges["edge_l"]]
        jacobi_list = self.generate_jacobi_list_for_element(vec_4)  # Jakobiany dla poszczególnych boków [uwzględniony warunek BC]
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        warunki_brzegowe = []                         # [dolna,prawa,gorna,lewa] jeżeli dotyczy
        for k,edge in enumerate(edges_list):          # dla kazdej krawedzi elementu
            wynik = np.zeros((1, 4))
            for i,point in enumerate(edge):           # przejdz przez punkty w krawedzi
                mat = np.zeros((1, 4))
                for j in range(4):                    # Wylicz dla konkretnego punktu funkcje ksztaltu
                    mat[0][j] = N[j](*point)
                if jacobi_list[k] != 0.0:
                    wynik += gauss[f"w{self.points}"][i] * self.alfa * mat * self.tot * jacobi_list[k]          # agreguj wynik
            warunki_brzegowe.append(wynik)

        return -np.sum(warunki_brzegowe, axis=0)
    def generate_jacobi_list_for_element(self,vec_4):
        if vec_4.to_list()[0].BC == 1 and vec_4.to_list()[1].BC == 1:
            jacobi_1 = np.sqrt((vec_4.to_list()[0].x - vec_4.to_list()[1].x) ** 2 + (vec_4.to_list()[0].y - vec_4.to_list()[1].y) ** 2) / 2
        else: jacobi_1 = 0.0  # """wyzeruje macierz - bo wtedy nie uwzgledniamy danej krawedzi [ Bez tego warunku wszystkie krawedzie sa zewnetrzne ]"""

        if vec_4.to_list()[1].BC == 1 and vec_4.to_list()[2].BC == 1:
            jacobi_2 = np.sqrt((vec_4.to_list()[1].x - vec_4.to_list()[2].x) ** 2 + (vec_4.to_list()[1].y - vec_4.to_list()[2].y) ** 2) / 2
        else: jacobi_2 = 0.0

        if vec_4.to_list()[2].BC == 1 and vec_4.to_list()[3].BC == 1:
            jacobi_3 = np.sqrt((vec_4.to_list()[2].x - vec_4.to_list()[3].x) ** 2 + (vec_4.to_list()[2].y - vec_4.to_list()[3].y) ** 2) / 2
        else: jacobi_3 = 0.0

        if vec_4.to_list()[3].BC == 1 and vec_4.to_list()[0].BC == 1:
            jacobi_4 = np.sqrt((vec_4.to_list()[3].x - vec_4.to_list()[0].x) ** 2 + (vec_4.to_list()[3].y - vec_4.to_list()[0].y) ** 2) / 2
        else: jacobi_4 = 0.0

        return [jacobi_1,jacobi_2,jacobi_3,jacobi_4]
    def get_vectorP_matrices(self):
        return self.VectorPs




