import os

class Paraview:
    def __init__(self,T_opt,global_data,grid,catalog_name,points):
        self.T_opt = T_opt
        self.global_data = global_data
        self.grid = grid
        self.SimulationTime = global_data["SimulationTime"]
        self.SimulationStepTime = global_data["SimulationStepTime"]
        self.path = os.getcwd() + "/data/Paraview/"
        self.points = points
        self.catalog_name = catalog_name

    def generate_paraview_files(self):
        num_nod = self.global_data["Nodes_number"]
        num_el = self.global_data["Elements_number"]
        num_wsp = len(self.grid.elements[0])

        for time in range(self.SimulationStepTime, self.SimulationTime + self.SimulationStepTime,self.SimulationStepTime):
            with open(self.path + f'{self.catalog_name}/{self.points}/sol_{time}.vtk', 'w') as file:
                file.write('# vtk DataFile Version 2.0\n')
                file.write('Unstructured Grid Example\n')
                file.write('ASCII\n')
                file.write('DATASET UNSTRUCTURED_GRID\n\n')
                file.write(f'POINTS {num_nod} float\n')

                for node in self.grid.nodes:
                    file.write(f'{node.x} {node.y} 0\n')

                file.write(f'\nCELLS {num_el } {num_el  * (num_wsp+1)}\n')

                for element in self.grid.elements:
                    ids = element.nodes_IDs
                    file.write(f"{num_wsp} {ids[0]} {ids[1]} {ids[2]} {ids[3]}\n")

                file.write(f'\nCELL_TYPES 9\n')
                for _ in range(num_el):
                    file.write('9\n')

                file.write(f'\nPOINT_DATA {num_nod}\n')
                file.write('SCALARS Temp float 1\n')
                file.write('LOOKUP_TABLE default\n')

                for tem in self.T_opt[int(time/self.SimulationStepTime)-1].flatten():
                    file.write(f'{tem}\n')


