from src.siatka import Global_Data,Grid
################################################################ TESTY

def test_1():
    print("---------------------------Test_1---------------------------")
    print("------------------------------------------------------------")
    global_data = Global_Data("./txt/Test1.txt")
    print(f'Test: SimulationTime: {global_data["SimulationTime"]} , Elements_number: {global_data["Elements_number"]}')
    print("------------")
    grid = Grid("./txt/Test1.txt")
    for i in range(len(grid.nodes)):
        print(f"{i+1}) x: {grid.node[i].x} y: {grid.node[i].y}")
    print("------------")
    for i in range(len(grid.elements)):
        print(f"{i+1}) vec[0]: {grid.elements[i].vec[0]} , vec[3]: {grid.elements[i].vec[3]}")

def test_2():
    print("---------------------------Test_2---------------------------")
    print("------------------------------------------------------------")
    global_data = Global_Data("./txt/Test2.txt")
    print(f'Test: SimulationTime: {global_data["SimulationTime"]} , Elements_number: {global_data["Elements_number"]}')
    grid = Grid("./txt/Test2.txt")
    for i in range(len(grid.nodes)):
        print(f"{i+1}) x: {grid.node[i].x} y: {grid.node[i].y}")
    print("------------")
    for i in range(len(grid.elements)):
        print(f"{i+1}) vec[0]: {grid.elements[i].vec[0]} , vec[3]: {grid.elements[i].vec[3]}")

def test_3():
    print("---------------------------Test_3---------------------------")
    print("------------------------------------------------------------")
    global_data = Global_Data("./txt/Test3.txt")
    print(f'Test: SimulationTime: {global_data["SimulationTime"]} , Elements_number: {global_data["Elements_number"]}')
    print("------------------------------------------------------------")
    grid = Grid("./txt/Test3.txt")
    for i in range(len(grid.nodes)):
        print(f"{i+1}) x: {grid.node[i].x} y: {grid.node[i].y}")
    print("------------")
    for i in range(len(grid.elements)):
        print(f"{i+1}) vec[0]: {grid.elements[i].vec[0]} , vec[3]: {grid.elements[i].vec[3]}")


