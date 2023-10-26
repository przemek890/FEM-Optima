from tests.test import test_write, test_integrate, test_jacobian
from src.jacobian import global_differentiation
""""""""""""""""""""""""""""""""""""""
path1 = "./data/txt/Test1.txt"
path2 = "./data/txt/Test2.txt"
path3 = "./data/txt/Test3.txt"
f_1 = lambda x: 5*(x**2) + 3*x + 6
f_2 = lambda x,y: 5*(x**2) * (y**2) + 3*x*y + 6
ksi , eta = 1.  , 1.
""""""""""""""""""""""""""""""""""""""
# test_write(path=path1)
# test_write(path=path2)
# test_write(path=path3)
# test_integrate(f1=f_1,f2=f_2)
# test_jacobian(path=path1)

print(f"\ndN/dx : {global_differentiation(ksi=ksi,eta=eta,path=path1)[0]}\n\n dN/dy : {global_differentiation(ksi=ksi,eta=eta,path=path1)[1]}")
