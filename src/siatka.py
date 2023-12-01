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
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
        self._BC = None

    def to_tuple(self):
        return (self._x, self._y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def BC(self):
        if self._BC is not None:
            return self._BC
        else:
            print("Dany element nie posiada jeszcze BC - zwrócono None")
            return None

    @BC.setter
    def BC(self, value):
        self._BC = value

class Element:
    def __init__(self,vec4: list):
        self.vec = vec4      # 4 - elementowa lista punktów
        self._matrix_H = None
        self._matrix_C = None
        self._matrix_HBC = None
        self._vectorP = None
        self._nodes_IDs = None

    def __getitem__(self, index):
        return self.vec[index]
    def __len__(self):
        return len(self.vec)

    def to_list(self):
        return self.vec

    @property
    def matrix_H(self):
        if self._matrix_H is not None:
            return self._matrix_H
        else:
            print("Dany element nie posiada jeszcze Macierzy H - zwrócono None")
            return None
    @matrix_H.setter
    def matrix_H(self, value):
        self._matrix_H = value


    @property
    def matrix_HBC(self):
        if self._matrix_HBC is not None:
            return self._matrix_HBC
        else:
            print("Dany element nie posiada jeszcze Macierzy H - zwrócono None")
            return None
    @matrix_HBC.setter
    def  matrix_HBC(self, value):
        self._matrix_HBC = value

    @property
    def matrix_C(self):
        if self._matrix_C is not None:
            return self._matrix_C
        else:
            print("Dany element nie posiada jeszcze Macierzy H - zwrócono None")
            return None
    @matrix_C.setter
    def  matrix_C(self, value):
        self._matrix_C = value

    @property
    def vectorP(self):
        if self._vectorP is not None:
            return self._vectorP
        else:
            print("Dany element nie posiada jeszcze vectorP - zwrócono None")
            return None
    @vectorP.setter
    def vectorP(self, value):
        self._vectorP = value


    @property
    def nodes_IDs(self):
        if self._nodes_IDs is not None:
            return self._nodes_IDs
        else:
            print("Dany element nie posiada jeszcze vectorP - zwrócono None")
            return None
    @nodes_IDs.setter
    def nodes_IDs(self, value):
        self._nodes_IDs = value

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
                        vec_4_points = [self.nodes[i-1] for i in vec_4]
                        vec_element = Element(vec_4_points)
                        vec_element.nodes_IDs = [int(x) - 1 for x in parts][1:] # Bo numerujemy od 0 w listach
                        self.elements.append(vec_element)

        """DODAWANIE FLAGI BC DO WEZŁA"""
        is_node_section = False
        with open(f"{self.file_path}", "r") as file:
            for line in file:
                if line.strip() == "*BC": is_node_section = True
                elif not line.strip(): is_node_section = False

                elif is_node_section and line.strip():
                    flags = [int(i) for i in line.strip().split(",")]
                    for j, node in enumerate(self.nodes):
                        if j + 1 in flags: node.BC = 1
                        else: node.BC = 0


    @property
    def node(self):
        return self.nodes

    @property
    def element(self):
        return self.elements


