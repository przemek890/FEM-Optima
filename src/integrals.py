import pandas as pd
from typing import Callable
import inspect
""""""""""""""""""""
def integration(f: Callable,dim:int,points: int,wezly: str = "./csv/wezly.csv"):
    """
    :param f: całkowana funkcja f(x) lub f(x,y)
    :param dim: rozmiar przestrzenii
    :param points: x punktowy schemat calkowania
    :param wezly: plik .csv z wezłami do kwadratury
    :return: wynik całki na przedziale [-1,1]
    """
    def wczytaj_wezly(file_path):
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        return df
    df = wczytaj_wezly(wezly)
    num_args = len(inspect.signature(f).parameters) # Zabezpieczenie przed funkcją o nieprawidłowej liczbie zmiennych

    if dim == 1 and points == 2 and num_args == 1:
        w1 = df.loc[(df['N'] == 1) & (df['k'] == 0)]["Ak"].values[0]
        w2 = df.loc[(df['N'] == 1) & (df['k'] == 1)]["Ak"].values[0]
        x1 = df.loc[(df['N'] == 1) & (df['k'] == 0)]["xk"].values[0]
        x2 = df.loc[(df['N'] == 1) & (df['k'] == 1)]["xk"].values[0]
        return w1 * f(x2) + w2 * f(x1)

    elif dim == 1 and points == 3 and num_args == 1:
        w1 = df.loc[(df['N'] == 2) & (df['k'] == 0)]["Ak"].values[0]
        w2 = df.loc[(df['N'] == 2) & (df['k'] == 1)]["Ak"].values[0]
        w3 = df.loc[(df['N'] == 2) & (df['k'] == 2)]["Ak"].values[0]
        x1 = df.loc[(df['N'] == 2) & (df['k'] == 0)]["xk"].values[0]
        x2 = df.loc[(df['N'] == 2) & (df['k'] == 1)]["xk"].values[0]
        x3 = df.loc[(df['N'] == 2) & (df['k'] == 2)]["xk"].values[0]

        return w1 * f(x1) + w2 * f(x2) + w3 * f(x3)

    elif dim == 2 and points == 2 and num_args == 2:
        w1 = df.loc[(df['N'] == 1) & (df['k'] == 0)]["Ak"].values[0]
        w2 = df.loc[(df['N'] == 1) & (df['k'] == 1)]["Ak"].values[0]
        x1 = df.loc[(df['N'] == 1) & (df['k'] == 0)]["xk"].values[0]
        x2 = df.loc[(df['N'] == 1) & (df['k'] == 1)]["xk"].values[0]

        return w1**2 * f(x2,x2) + w1*w2 * f(x1,x2) + w2**2 * f(x1,x1) + w1*w2 * f(x2,x1)

    elif dim == 2 and points == 3 and num_args == 2:
        w1 = df.loc[(df['N'] == 2) & (df['k'] == 0)]["Ak"].values[0]
        w2 = df.loc[(df['N'] == 2) & (df['k'] == 1)]["Ak"].values[0]
        w3 = df.loc[(df['N'] == 2) & (df['k'] == 2)]["Ak"].values[0]
        x1 = df.loc[(df['N'] == 2) & (df['k'] == 0)]["xk"].values[0]
        x2 = df.loc[(df['N'] == 2) & (df['k'] == 1)]["xk"].values[0]
        x3 = df.loc[(df['N'] == 2) & (df['k'] == 2)]["xk"].values[0]

        return (w1**2 * f(x3,x3) + w1*w2 * f(x3,x2) + w1*w3 * f(x3,x1) +
        + w2*w1 * f(x2,x3) + w2**2 * f(x2,x2) + w2*w3 * f(x2,x1) +
        + w3*w1 * f(x1,x3) + w3*w2 * f(x1,x2) + w3**2 * f(x1,x1))

    else:
        print("Błąd całkowania")
        pass


