import numpy as np
import copy
from src.siatka import Grid
from src.integrals import integration
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def funkcja(ksi,eta,vec4,node_i,is_x):
    dxde = lambda vec4, eta: 0.25 * eta * (vec4[0].x - vec4[1].x + vec4[2].x - vec4[3].x) + 0.25 * (- vec4[0].x + vec4[1].x + vec4[2].x - vec4[3].x)
    dyde = lambda vec4, eta: 0.25 * eta * (vec4[0].y - vec4[1].y + vec4[2].y - vec4[3].y) + 0.25 * (- vec4[0].y + vec4[1].y + vec4[2].y - vec4[3].y)
    dxdn = lambda vec4, ksi: 0.25 * ksi * (vec4[0].x - vec4[1].x + vec4[2].x - vec4[3].x) + 0.25 * (- vec4[0].x - vec4[1].x + vec4[2].x + vec4[3].x)
    dydn = lambda vec4, ksi: 0.25 * ksi * (vec4[0].y - vec4[1].y + vec4[2].y - vec4[3].y) + 0.25 * (- vec4[0].y - vec4[1].y + vec4[2].y + vec4[3].y)

    if node_i == 0:
        Nide = -0.25 * (1 - eta); Nidn = -0.25 * (1 - ksi)
    elif node_i == 1:
        Nide = 0.25 * (1 - eta); Nidn = -0.25 * (1 - ksi)
    elif node_i == 2:
        Nide = 0.25 * (1 - eta); Nidn = 0.25 * (1 - ksi)
    elif node_i == 3:
        Nide = -0.25 * (1 - eta); Nidn = 0.25 * (1 - ksi)
    else:
        print("error")
        exit(-1)

    matrix = np.array([[dxde(vec4, eta), dxdn(vec4, ksi)], [dyde(vec4, eta), dydn(vec4, ksi)]])

    determinant = np.linalg.det(matrix)
    reverse_mat = np.array([[dydn(vec4, ksi), -dxdn(vec4, ksi)], [-dyde(vec4, eta), dxde(vec4, eta)]])
    vec_p = np.array([Nide, Nidn])

    wynik = matrix @ ((1./ determinant) * reverse_mat @ vec_p)

    if is_x is True: return wynik[0]
    else: return wynik[1]
def model(path):
    new_elements = []

    grid = Grid(path)
    for vec4 in grid.elements:  # dla każdego wektora
        element = []
        for i in range(4):      # dla kazdej krotki punktowej w wektorze
            x_new = integration(lambda ksi, eta: funkcja(ksi, eta, vec4, i, is_x=True), 2, 4)
            y_new = integration(lambda ksi, eta: funkcja(ksi, eta, vec4, i, is_x=False), 2, 4)
            element.append((x_new,y_new))

        new_elements.append(element)
    return new_elements
