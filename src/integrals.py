from typing import Callable
import inspect
from Data.Gauss_points import gauss
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
