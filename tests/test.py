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