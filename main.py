from tests.test import *
import os
""""""""""""""""""""""""""""""""""""""
path1 = "./data/txt/Test1.txt"
path2 = "./data/txt/Test2.txt"
path3 = "./data/txt/Test3.txt"
f_1 = lambda x: 5*(x**2) + 3*x + 6
f_2 = lambda x,y: 5*(x**2) * (y**2) + 3*x*y + 6
""""""""""""""""""""""""""""""""""""""
# test_write(path=path1)
# test_write(path=path2)
# test_write(path=path3)
# test_integrate(f1=f_1,f2=f_2)
# test_element_uniwersalny()
# test_macierz_H(path2,points=2)
# test_macierz_HBC(points=2,grid=Grid(path2),global_data=Global_Data(path2))
""""""""""""""""""""""""""""""""""""""""" ""MAIN"""

import os
import easygui

def get_txt(grid_list):
    msg = "Wybierz plik:"
    title = "Wybór pliku"
    txt = easygui.choicebox(msg, title, grid_list)
    return txt

def get_points():
    msg = "Wybierz schemat punktowy:"
    title = "Wybór schematu punktowego"
    lista_schematow = ["2", "3", "4"]
    points = easygui.choicebox(msg, title, lista_schematow)
    return int(points)
def main():
    grid_list = os.listdir("./data/txt")
    txt = get_txt(grid_list)
    points = get_points()

    path = os.getcwd() + f"/data/txt/{txt}"
    global_data = Global_Data(path)                             # Dane globalne
    grid = Grid(path)                                           # Utworz siatkę

    matrix_H = Matrix_H(points,path)                            # Uzyskaj macierze sztywności H dla wszystkich elementów
    matrix_HBC = Matrix_HBC(points,grid,global_data)            # Uzyskaj macierze HBC dla wszystkich elementów
    matrix_vecP = VectorP(points,grid,global_data)


    for i,element in enumerate(grid.elements):
        element.matrix_H = matrix_H.get_H_matrices()[i]             # Dodaj macierz H do elementów
        element.matrix_HBC = matrix_HBC.get_HBC_matrices()[i]       # Dodaj macierz HBC do elementów
        element.vectorP = matrix_vecP.get_vectorP_matrices()[i]     # Dodaj VectorP do elementów

    # print(f"\033[94m*************************MACIERZ_HBC*************************\033[0m")
    # for element in grid.elements:
    #     print(element.matrix_HBC)
    # print(f"\033[94m*************************************************************\033[0m")

    print(f"\033[94m*************************MACIERZ_VECTOR_P*************************\033[0m")
    for element in grid.elements:
        print(element.vectorP)
    print(f"\033[94m*************************************************************\033[0m")


if __name__ == "__main__":
    main()

