"""SimulationTime = global_data["SimulationTime"] gdzie global_data to obiekt klasy Global_Data"""
class Global_Data:
    '''
    --> Dostępne pola:
    SimulationTime // SimulationStepTime
    Conductivity // Alfa
    Tot // InitialTemp
    Density // SpecificHeat
    Nodes_number // Elements_number
    '''
    def __init__(self,file_PATH: str):
        variables = {}
        self.file_path = file_PATH
        with open(f'{self.file_path}', 'r') as file:
            for i in range(10):
                line = file.readline()
                parts = line.split()

                if len(parts) == 2:
                    variable_name = parts[0]
                    variable_value = parts[1]
                    variables[variable_name] = int(variable_value)

                if len(parts) == 3:
                    variable_name = f"{parts[0]}_{parts[1]}"
                    variable_value = parts[2]
                    variables[variable_name] = int(variable_value)

        self.variables = variables

    def __getitem__(self, key: str) -> int:
        return self.variables.get(key, None)

class Node:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y
class Element:
    def __init__(self,vec_4:list[4]):
        self.vec = vec_4

"""x = grid.nodes[i].x el_4 = grid.elements[i].vec[j]"""
class Grid:
    def __init__(self,file_PATH: str):
        self.file_path = file_PATH

        self.nodes = []
        self.elements = []

        """TWORZENIE LISTY NODE'ÓW"""
        is_node_section = False
        with open(f"{self.file_path}", "r") as file:
            for line in file:
                if line.strip() == "*Node": is_node_section = True
                elif line.strip().split(',')[0] == "*Element": is_node_section = False

                elif is_node_section and line.strip():
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        x, y = float(parts[1].strip()), float(parts[2].strip())
                        self.nodes.append(Node(x,y))

        """TWORZENIE LISTY ELEMENTÓW"""
        is_element_section = False
        with open(f"{self.file_path}", "r") as file:
            for line in file:
                if line.strip().split(',')[0] == "*Element": is_element_section = True
                elif line.strip() == "*BC": is_element_section = False

                elif is_element_section and line.strip():
                    parts = line.strip().split(",")
                    if len(parts) == 5:
                        vec_4 = [int(x) for x in parts][1:]
                        self.elements.append(Element(vec_4))

    @property
    def node(self):
        return self.nodes

    @property
    def element(self):
        return self.elements


