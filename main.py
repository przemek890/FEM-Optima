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
# test_macierz_HBC(points=2,grid=Grid(path3),global_data=Global_Data(path3))
""""""""""""""""""""""""""""""""""""""""" ""MAIN"""

def get_txt(grid_list):
    while True:
        for file in grid_list: print(f"[ \033[91m{file} \033[0m]")
        txt = str(input("Podaj nazwę pliku z siatkami: "))
        if txt in grid_list:
            return txt
        print("Błędna nazwa pliku z siatkami - spróbuj ponownie!")
def get_points():
    while True:
        lista_schematow = [2,3,4]
        for i in lista_schematow: print(f"[ \033[94m{i} \033[0m]")
        points = int(input("Podaj schemat punktowy dla siatki: "))
        if points in [2, 3, 4]:
            return points
        print("Błędny schemat punktowy - spróbuj ponownie!")
def main():
    grid_list = os.listdir("./data/txt")
    txt = get_txt(grid_list)
    points = get_points()

    path = os.getcwd() + f"/data/txt/{txt}"
    global_data = Global_Data(path)                             # Dane globalne
    grid = Grid(path)                                           # Utworz siatkę

    matrix_H = Matrix_H(points,path)                            # Uzyskaj macierze sztywności H dla wszystkich elementów
    matrix_HBC = Matrix_HBC(points,grid,global_data)


    for i,element in enumerate(grid.elements):
        element.matrix_H = matrix_H.get_H_matrices()[i]         # Dodaj macierz H do elementów
        element.matrix_HBC = matrix_HBC.get_HBC_matrices()[i]       # Dodaj macierz HBC do elementów
        # print(element.matrix_H )
        # print(element.matrix_H )

    print(grid.elements[0].matrix_HBC)


if __name__ == "__main__":
    main()

