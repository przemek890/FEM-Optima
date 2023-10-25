from typing import Callable
import inspect
import numpy as np
""""""""""""""""""""
points_2 = [np.sqrt(1/3),-np.sqrt(1/3)]
weights_2 = [1.0,1.0]
points_3 = [np.sqrt(3/5),0,-np.sqrt(3/5)]
weights_3 = [5/9,8/9,5/9]
points_4 = [np.sqrt(3/7 + 2/7 * np.sqrt(6/5)),np.sqrt(3/7 - 2/7 * np.sqrt(6/5)),-np.sqrt(3/7 - 2/7 * np.sqrt(6/5)),-np.sqrt(3/7 + 2/7 * np.sqrt(6/5))]
weights_4 = [(18 - np.sqrt(30))/ 36,(18 + np.sqrt(30))/ 36,(18 + np.sqrt(30))/ 36,(18 - np.sqrt(30))/ 36]
gauss = {"w2":weights_2,"p2":points_2,"w3":weights_3,"p3":points_3,"w4":weights_4,"p4":points_4}
""""""""""""""""""""
def integration(f: Callable,dim:int,points: int):
    wynik = 0
    num_args = len(inspect.signature(f).parameters) # Zabezpieczenie przed funkcją o nieprawidłowej liczbie zmiennych
    assert dim == num_args, "Niezgodność rozmiaru przestrzeni i zmiennych przyjmowanych przez funkcje"

    if dim == 1 and points == 2 and num_args == 1:
        for w, x in zip(gauss["w2"], gauss["p2"]):
            wynik += w * f(x)
        return wynik
    elif dim == 1 and points == 3 and num_args == 1:
        for w,x in zip(gauss["w3"],gauss["p3"]):
            wynik += w * f(x)
        return wynik
    elif dim == 1 and points == 4 and num_args == 1:
        for w, x in zip(gauss["w4"], gauss["p4"]):
            wynik += w * f(x)
        return wynik

    elif dim == 2 and points == 2 and num_args == 2:
        for w1, x1 in zip(gauss["w2"], reversed(gauss["p2"])):
            for w2, x2 in zip(gauss["w2"], reversed(gauss["p2"])):
                wynik += w1 * w2 * f(x2,x1)
        return wynik
    elif dim == 2 and points == 3 and num_args == 2:
        for w1, x1 in zip(gauss["w3"], reversed(gauss["p3"])):
            for w2, x2 in zip(gauss["w3"], reversed(gauss["p3"])):
                wynik += w1 * w2 * f(x2,x1)
        return wynik
    elif dim == 2 and points == 4 and num_args == 2:
        for w1, x1 in zip(gauss["w4"], reversed(gauss["p4"])):
            for w2, x2 in zip(gauss["w4"], reversed(gauss["p4"])):
                wynik += w1 * w2 * f(x2,x1)
        return wynik

    else:
        raise Exception("Brak implementacji dla zadanych parametrów kwadratury")