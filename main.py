from src.tests.test import *
from src.Aggregation import Aggregation
from src.Solver import Solver
from src.Paraview import Paraview
import easygui
import os
import sys
import time
""""""""""""""""""""""""""""""""""""""
path3 = "./Data/txt/Simulation.txt"
f_1 = lambda x: 5 * (x ** 2) + 3 * x + 6
f_2 = lambda x, y: 5 * (x ** 2) * (y ** 2) + 3 * x * y + 6
""""""""""""""""""""""""""""""""""""""
# test_write(path=path1)
# test_write(path=path2)
# test_write(path=path3)
# test_integrate(f1=f_1,f2=f_2)
# test_element_uniwersalny()
# test_macierz_H(path2,points=2)
# test_macierz_HBC(points=2,grid=Grid(path2),global_data=Global_Data(path2))
# test_vectorP(points=2,grid=Grid(path2),global_data=Global_Data(path2))
# test_macierz_C(path2,points=2)
""""""""""""""""""""""""""""""""""""""""" ""MAIN"""
def get_txt():
    return "Simulation.txt"
def get_points():
    msg = "Wybierz schemat punktowy:"
    title = "Schemat całkowania"
    lista_schematow = ["2", "3", "4"]
    points = easygui.choicebox(msg, title, lista_schematow)
    if points is None:
        sys.exit()
    return int(points)


def main():
    grid_list = os.listdir("./Data/txt")
    txt = get_txt()
    points = get_points()

    path = os.getcwd() + f"/Data/txt/{txt}"
    global_data = Global_Data(path)  # Dane globalne
    grid = Grid(path)                # Utworz siatkę

    t1 = time.time()
    matrix_H = Matrix_H(points, path)                   # Uzyskaj macierze sztywności H dla wszystkich elementów
    matrix_HBC = Matrix_HBC(points, grid, global_data)  # Uzyskaj macierze HBC dla wszystkich elementów
    matrix_vecP = VectorP(points, grid, global_data)    # Uzyskaj wektor P dla wszystkich elementów
    matrix_C = Matrix_C(points, path)                   # Uzyskaj macierz C dla wszystkich elementów

    for i, element in enumerate(grid.elements):
        element.matrix_H = matrix_H.get_H_matrices()[i]          # Dodaj macierz H do elementów
        element.matrix_HBC = matrix_HBC.get_HBC_matrices()[i]    # Dodaj macierz HBC do elementów
        element.vectorP = matrix_vecP.get_vectorP_matrices()[i]  # Dodaj VectorP do elementów
        element.matrix_C = matrix_C.get_C_matrices()[i]          # Dodaj Macierz C do elementów


    aggregate = Aggregation(grid, global_data)       # Klasa do agregacji macierzy
    # aggregate.test_H_global()                      # Test złożenia macierzy H_global
    # aggregate.test_P_global()                      # Test złożenia wektora  P_global
    # aggregate.test_C_global()                      # Test złożenia macierzy C_global


    solver = Solver(global_data,aggregate.global_H,aggregate.global_P,aggregate.global_C)       # Klasa do rozwiązywania układu równań
    t_opt = solver.solve()                                                                      # Rozwiązanie układu równań

    t2 = time.time()

    print(f"Czas obliczeń: {t2-t1} s")

    paraview = Paraview(t_opt,global_data,grid,f"{txt.split('.')[0]}",points)
    paraview.generate_paraview_files()



def multiply_floats(line):
    parts = line.split(',')
    for i in range(1, len(parts)):
        try:
            value = float(parts[i])
            parts[i] = str(value * 4)
        except ValueError:
            pass
    return ','.join(parts)
def process_section(lines):
    new_lines = []
    for i in range(0, len(lines), 3):
        new_lines.extend(multiply_floats(line) for line in lines[i:i + 3])
    return '\n'.join(new_lines)

if __name__ == "__main__":
    main()



