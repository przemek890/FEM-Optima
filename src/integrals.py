import pandas as pd
from typing import Callable
import inspect
import numpy as np
""""""""""""""""""""
""""""""""""""""""""
def integration(f: Callable,dim:int,points: int,):
    num_args = len(inspect.signature(f).parameters) # Zabezpieczenie przed funkcją o nieprawidłowej liczbie zmiennych
    assert dim == num_args, "Niezgodność rozmiaru przestrzeni i zmiennych przyjmowanych przez funkcje"
    if dim == 1 and points == 2 and num_args == 1:
        w11 = 1.0
        w21 = w11
        x11 = np.sqrt(1/3)
        x21 = -x11
        return w11 * f(x21) + w21 * f(x11)
    elif dim == 1 and points == 3 and num_args == 1:
        w11 = 5/9
        w21 = 8/9
        w31 = 5/9
        x11 = np.sqrt(3/5)
        x21 = 0
        x31 = -x11
        return w11 * f(x11) + w21 * f(x21) + w31 * f(x31)
    elif dim == 1 and points == 4 and num_args == 1:
        w11 = (18 - np.sqrt(30))/ 36
        w21 = (18 + np.sqrt(30))/ 36
        w31 = w21
        w41 = w11
        x11 = np.sqrt(3/7 + 2/7 * np.sqrt(6/5))
        x21 = np.sqrt(3/7 - 2/7 * np.sqrt(6/5))
        x31 = - x21
        x41 = - x11
        return w11 * f(x11) + w21 * f(x21) + w31 * f(x31) + w41 * f(x41)
    elif dim == 2 and points == 2 and num_args == 2:
        w11 = 1.0
        w21 = w11
        x11 = np.sqrt(1 / 3)
        x21 = -x11
        return w11**2 * f(x21,x21) + w11*w21 * f(x11,x21) + w21**2 * f(x11,x11) + w11*w21 * f(x21,x11)
    elif dim == 2 and points == 3 and num_args == 2:
        w11 = 5/9
        w21 = 8/9
        w31 = 5/9
        x11 = np.sqrt(3/5)
        x21 = 0
        x31 = -x11
        return (w11**2 * f(x31,x31) + w11*w21 * f(x31,x21) + w11*w31 * f(x31,x11) +
        + w21*w11 * f(x21,x31) + w21**2 * f(x21,x21) + w21*w31 * f(x21,x11) +
        + w31*w11 * f(x11,x31) + w31*w21 * f(x11,x21) + w31**2 * f(x11,x11))
    elif dim == 2 and points == 4 and num_args == 2:
        w11 = (18 - np.sqrt(30))/ 36
        w21 = (18 + np.sqrt(30))/ 36
        w31 = w21
        w41 = w11
        x11 = np.sqrt(3/7 + 2/7 * np.sqrt(6/5))
        x21 = np.sqrt(3/7 - 2/7 * np.sqrt(6/5))
        x31 = - x21
        x41 = - x11
        return (w11**2 * f(x41, x41) + w11 * w21 * f(x41, x31) + w11 * w31 * f(x41, x21) + w11 * w41 * f(x41, x11) +
                + w21 * w11 * f(x31, x41) + w21**2 * f(x31, x31) + w21 * w31 * f(x31, x21) + w21 * w41 * f(x31, x11) +
                + w31 * w11 * f(x21, x41) + w31 * w21 * f(x21, x31) + w31**2 * f(x21, x21) + w31 * w41 * f(x21, x11) +
                + w41 * w11 * f(x11, x41) + w41 * w21 * f(x11, x31) + w41 * w31 * f(x11, x21) + w41**2 * f(x11, x11))
    else:
        raise Exception("Brak implementacji dla zadanych parametrów kwadratury")