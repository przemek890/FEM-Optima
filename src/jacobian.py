import numpy as np
from src.siatka import Grid
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def jacobian(ksi,eta,vec4,node_i):
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

    wynik = (1./ determinant) * reverse_mat @ vec_p

    return tuple(wynik)

def global_differentiation(ksi,eta,path):
    new_elements_x = []
    new_elements_y = []
    grid = Grid(path)
    for vec4 in grid.elements:  # dla każdego wektora
        element_x = []
        element_y = []
        for i in range(4):      # dla kazdej krotki punktowej w wektorze
            xy_new = jacobian(ksi=ksi,eta=eta,vec4=vec4,node_i=i)
            element_x.append(xy_new[0])
            element_y.append(xy_new[1])

        new_elements_x.append(tuple(element_x))
        new_elements_y.append(tuple(element_y))
    return  new_elements_x,  new_elements_y
