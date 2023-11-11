from data.Gauss_points import gauss_points
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
test_macierz_H(path1,points=2)
""""""""""""""""""""""""""""""""""""""

"""""MAIN"""
def get_grid(grid_list):
    while True:
        grid = str(input("Podaj nazwę pliku z siatkami: "))
        if grid in grid_list:
            return grid
        print("Błędna nazwa pliku z siatkami - spróbuj ponownie!")
def get_points():
    while True:
        points = int(input("Podaj schemat punktowy dla siatki: "))
        if points in [2, 3, 4]:
            return points
        print("Błędny schemat punktowy - spróbuj ponownie!")
def main():
    grid_list = os.listdir("./data/txt")
    grid = get_grid(grid_list)
    points = get_points()

    grid_path = os.getcwd() + f"/data/txt/{grid}"
    matrix_H = Matrix_H(points,grid_path)                   # Uzyskaj macierze sztywności H dla wszystkich elementów
    grid = Grid(grid_path)                                  # Utworz siatkę
    for i,element in enumerate(grid.elements):
        element.matrix_H = matrix_H.get_H_matrices()[i]
if __name__ == "__main__":
    main()


