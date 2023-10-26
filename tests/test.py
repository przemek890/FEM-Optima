from src.siatka import Global_Data,Grid
from src.integrals import integration
""""""""""""""""""""""""""""""""""""""""""
def test_write(path):
    print("---------------------------Test_1---------------------------")
    print("------------------------------------------------------------")
    global_data = Global_Data(path)
    print(f'Test: SimulationTime: {global_data["SimulationTime"]} , Elements_number: {global_data["Elements_number"]}')
    print("------------")
    grid = Grid(path)
    for i in range(len(grid.nodes)):
        print(f"{i+1}) x: {grid.node[i].x} y: {grid.node[i].y}")
    print("------------")
    for i in range(len(grid.elements)):
        print(f"{i+1}) vec[0]: {grid.elements[i].vec[0].to_tuple()} , vec[3]: {grid.elements[i].vec[3].to_tuple()}")
def test_integrate(f1,f2):
    print("---------------------------INTEGRATION_TEST---------------------------")
    wyn_1 = integration(f=f1,dim=1,points=2)
    wyn_2 = integration(f=f1, dim=1, points=3)
    wyn_3 = integration(f=f1, dim=1, points=4)

    wyn_4 = integration(f=f2,dim=2,points=2)
    wyn_5 = integration(f=f2, dim=2, points=3)
    wyn_6 = integration(f=f2, dim=2, points=4)
    print(f"d1/p2: {wyn_1}\nd1/p3: {wyn_2}\nd1/p4: {wyn_3}\nd2/p2: {wyn_4}\nd2/p3: {wyn_5}\nd2/p4: {wyn_6}")
    print("------------")
def test_jacobian(path):
    def f_test(ksi, eta, vec4, node_i, is_ksi):
        import numpy as np
        dxde = lambda vec4, eta: 0.25 * eta * (vec4[0].x - vec4[1].x + vec4[2].x - vec4[3].x) + 0.25 * (
                    - vec4[0].x + vec4[1].x + vec4[2].x - vec4[3].x)
        dyde = lambda vec4, eta: 0.25 * eta * (vec4[0].y - vec4[1].y + vec4[2].y - vec4[3].y) + 0.25 * (
                    - vec4[0].y + vec4[1].y + vec4[2].y - vec4[3].y)
        dxdn = lambda vec4, ksi: 0.25 * ksi * (vec4[0].x - vec4[1].x + vec4[2].x - vec4[3].x) + 0.25 * (
                    - vec4[0].x - vec4[1].x + vec4[2].x + vec4[3].x)
        dydn = lambda vec4, ksi: 0.25 * ksi * (vec4[0].y - vec4[1].y + vec4[2].y - vec4[3].y) + 0.25 * (
                    - vec4[0].y - vec4[1].y + vec4[2].y + vec4[3].y)

        if node_i == 0:
            Nide = -0.25 * (1 - eta);
            Nidn = -0.25 * (1 - ksi)
        elif node_i == 1:
            Nide = 0.25 * (1 - eta);
            Nidn = -0.25 * (1 - ksi)
        elif node_i == 2:
            Nide = 0.25 * (1 - eta);
            Nidn = 0.25 * (1 - ksi)
        elif node_i == 3:
            Nide = -0.25 * (1 - eta);
            Nidn = 0.25 * (1 - ksi)
        else:
            print("error")
            exit(-1)

        matrix = np.array([[dxde(vec4, eta), dxdn(vec4, ksi)], [dyde(vec4, eta), dydn(vec4, ksi)]])

        determinant = np.linalg.det(matrix)
        reverse_mat = np.array([[dydn(vec4, ksi), -dxdn(vec4, ksi)], [-dyde(vec4, eta), dxde(vec4, eta)]])
        vec_p = np.array([Nide, Nidn])

        wynik = matrix @ ((1. / determinant) * reverse_mat @ vec_p)

        if is_ksi is True: return wynik[0]
        else: return wynik[1]
    """"""""""""""""""""""""""""""""""""""""""
    new_elements_ksi = []
    new_elements_eta = []

    grid = Grid(path)
    for vec4 in grid.elements:  # dla każdego wektora
        element_ksi = []
        element_eta = []
        for i in range(4):      # dla kazdej krotki punktowej w wektorze
            x_new = integration(lambda ksi, eta: f_test(ksi, eta, vec4, i, is_ksi=True), 2, 4)
            y_new = integration(lambda ksi, eta: f_test(ksi, eta, vec4, i, is_ksi=False), 2, 4)
            element_ksi.append(x_new)
            element_eta.append(y_new)

        new_elements_ksi.append(tuple(element_ksi))
        new_elements_eta.append(tuple(element_eta))
    print("ksi elements test: ", new_elements_ksi)
    print("\n\neta elements test: ", new_elements_eta)
    # Jeżeli pary punktów są blisko: (-1,-1), (1,-1), (1,1), (-1,1) to poprawne przekształcenie na układ lokalny
