from multipledispatch import dispatch


class Vertex:
    '''
    Class to create a vertex object
    '''

    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:
    '''
    Class to create an edge object
    '''

    def __init__(self, v1: Vertex, v2: Vertex):
        self.v1 = v1
        self.v2 = v2

    def __repr__(self):
        return f'({self.v1} to {self.v2})'

    def __str__(self):
        return f'({self.v1} to {self.v2})'

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2


class DirectedGraph:
    '''
    Class to create a graph object
    G = (V, E) where V = {v_1, v_2, v_3, ..., v_n} and E = {(v_i, v_j)}
    '''

    def __init__(self):
        self.graph_dict = {}

    @dispatch(Vertex)
    def add_vertex(self, vertex: Vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
        else:
            raise ValueError('Vertex already exists')

    @dispatch(str)
    def add_vertex(self, name: str):
        self.add_vertex(Vertex(name))

    @dispatch(Edge)
    def add_edge(self, edge: Edge):

        v1 = edge.get_v1()
        v2 = edge.get_v2()

        if edge.get_v1() not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} does not exist')
        if edge.get_v2() not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} does not exist')

        self.graph_dict[v1].append(v2)

    @dispatch(str, str)
    def add_edge(self, name1: str, name2: str):
        self.add_edge(Edge(self.get_vertex(name1), self.get_vertex(name2)))

    @dispatch(Vertex)
    def neighbors(self, vertex: Vertex):
        return self.graph_dict[vertex]

    @dispatch(str)
    def neighbors(self, name: str):
        return self.neighbors(self.get_vertex(name))

    def is_vertex_in(self, vertex: Vertex):
        return vertex in self.graph_dict

    def get_vertex(self, name: str):
        for vertex in self.graph_dict:
            if vertex.get_name() == name:
                return vertex
        print(f'Vertex {name} does not exist')
        return None

    @dispatch(Vertex, Vertex)
    def bfs(self, start: Vertex, end: Vertex):
        '''
        Breadth-first search algorithm
        '''
        if not self.is_vertex_in(start):
            assert ValueError(f'Vertex {start.get_name()} does not exist')

        if not self.is_vertex_in(end):
            assert ValueError(f'Vertex {end.get_name()} does not exist')

        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.neighbors(node):

                if adjacent not in path:
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)

    @dispatch(str, str)
    def bfs(self, start: str, end: str):
        '''
        Breadth-first search algorithm
        '''
        return self.bfs(self.get_vertex(start), self.get_vertex(end))

    @dispatch(Vertex, Vertex)
    def dfs(self, start: Vertex, end: Vertex):
        '''
        Depth-first search algorithm
        '''
        if not self.is_vertex_in(start):
            assert ValueError(f'Vertex {start.get_name()} does not exist')

        if not self.is_vertex_in(end):
            assert ValueError(f'Vertex {end.get_name()} does not exist')

        stack = []
        stack.append([start])
        while stack:
            path = stack.pop(-1)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.neighbors(node):
                if adjacent not in path:
                    new_path = list(path)
                    new_path.append(adjacent)
                    stack.append(new_path)

    @dispatch(str, str)
    def dfs(self, start: str, end: str):
        '''
        Depth-first search algorithm
        '''
        return self.dfs(self.get_vertex(start), self.get_vertex(end))

    def __call__(self, name: str):
        return self.get_vertex(name)

    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += f'{v1.get_name()} -> {v2.get_name()}\n'
        return all_edges


class UndirectedGraph(DirectedGraph):

    @dispatch(Edge)
    def add_edge(self, edge: Edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()

        if edge.get_v1() not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} does not exist')
        if edge.get_v2() not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} does not exist')

        self.graph_dict[v1].append(v2)
        self.graph_dict[v2].append(v1)

    @dispatch(str, str)
    def add_edge(self, name1: str, name2: str):
        self.add_edge(Edge(self.get_vertex(name1), self.get_vertex(name2)))

    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += f'{v1.get_name()} <-> {v2.get_name()}\n'
        return all_edges


def build_graph():
    g = UndirectedGraph()

    # All 32 mexican states from north to south

    states = ['Sonora', 'Chihuahua', 'Coahuila', 'Nuevo Leon', 'Guerrero',
              'San Luis Potosi', 'Zacatecas', 'Durango', 'Nayarit', 'Jalisco',
              'Aguascalientes', 'Guanajuato', 'Michoacan', 'Colima', 'Ciudad de Mexico',
              'Morelos', 'Puebla', 'Hidalgo', 'Tlaxcala', 'Queretaro', 'Mexico',
              'Veracruz', 'Tamaulipas', 'Chiapas', 'Tabasco', 'Campeche', 'Quintana Roo',
              'Yucatan', 'Baja California Sur', 'Baja California', 'Sinaloa', 'Oaxaca']

    for state in states:
        g.add_vertex(state)

    # Add an edge between each neighboring state
    g.add_edge("Baja California Sur", "Baja California")

    g.add_edge("Baja California", "Sonora")

    g.add_edge("Sonora", "Chihuahua")
    g.add_edge("Sonora", "Sinaloa")

    g.add_edge("Chihuahua", "Coahuila")
    g.add_edge("Chihuahua", "Sinaloa")
    g.add_edge("Chihuahua", "Durango")

    g.add_edge("Coahuila", "Durango")
    g.add_edge("Coahuila", "Nuevo Leon")
    g.add_edge("Coahuila", "Zacatecas")
    g.add_edge("Coahuila", "San Luis Potosi")

    g.add_edge("Nuevo Leon", "Zacatecas")
    g.add_edge("Nuevo Leon", "San Luis Potosi")
    g.add_edge("Nuevo Leon", "Tamaulipas")

    g.add_edge("Tamaulipas", "San Luis Potosi")
    g.add_edge("Tamaulipas", "Veracruz")

    g.add_edge("Sinaloa", "Durango")
    g.add_edge("Sinaloa", "Nayarit")

    g.add_edge("Durango", "Nayarit")
    g.add_edge("Durango", "Zacatecas")

    g.add_edge("Zacatecas", "Nayarit")
    g.add_edge("Zacatecas", "Jalisco")
    g.add_edge("Zacatecas", "Aguascalientes")
    g.add_edge("Zacatecas", "Guanajuato")
    g.add_edge("Zacatecas", "San Luis Potosi")

    g.add_edge("San Luis Potosi", "Guanajuato")
    g.add_edge("San Luis Potosi", "Queretaro")
    g.add_edge("San Luis Potosi", "Hidalgo")
    g.add_edge("San Luis Potosi", "Veracruz")

    g.add_edge("Nayarit", "Jalisco")

    g.add_edge("Jalisco", "Colima")
    g.add_edge("Jalisco", "Michoacan")
    g.add_edge("Jalisco", "Guanajuato")

    g.add_edge("Aguascalientes", "Jalisco")

    g.add_edge("Guanajuato", "Michoacan")
    g.add_edge("Guanajuato", "Queretaro")

    g.add_edge("Queretaro", "Michoacan")
    g.add_edge("Queretaro", "Mexico")
    g.add_edge("Queretaro", "Hidalgo")

    g.add_edge("Hidalgo", "Michoacan")
    g.add_edge("Hidalgo", "Mexico")
    g.add_edge("Hidalgo", "Tlaxcala")
    g.add_edge("Hidalgo", "Puebla")
    g.add_edge("Hidalgo", "Veracruz")

    g.add_edge("Colima", "Michoacan")

    g.add_edge("Michoacan", "Guerrero")
    g.add_edge("Michoacan", "Mexico")

    g.add_edge("Mexico", "Guerrero")
    g.add_edge("Mexico", "Morelos")
    g.add_edge("Mexico", "Ciudad de Mexico")
    g.add_edge("Mexico", "Tlaxcala")
    g.add_edge("Mexico", "Puebla")

    g.add_edge("Guerrero", "Oaxaca")
    g.add_edge("Guerrero", "Morelos")
    g.add_edge("Guerrero", "Puebla")

    g.add_edge("Morelos", "Ciudad de Mexico")
    g.add_edge("Morelos", "Puebla")

    g.add_edge("Puebla", "Oaxaca")
    g.add_edge("Puebla", "Veracruz")
    g.add_edge("Puebla", "Tlaxcala")

    g.add_edge("Oaxaca", "Veracruz")
    g.add_edge("Oaxaca", "Chiapas")

    g.add_edge("Chiapas", "Tabasco")
    g.add_edge("Chiapas", "Veracruz")

    g.add_edge("Tabasco", "Veracruz")
    g.add_edge("Tabasco", "Campeche")

    g.add_edge("Campeche", "Yucatan")
    g.add_edge("Campeche", "Quintana Roo")

    g.add_edge("Yucatan", "Quintana Roo")

    return g


if __name__ == '__main__':
    g = build_graph()

    state_1 = input('Enter the name of the first state: ')
    state_2 = input('Enter the name of the second state: ')

    print("BFS")
    path = g.bfs(state_1, state_2)
    for state in path:
        print(state)

    print("\n")
    print("-" * 20, end="\n\n")

    print("DFS")
    path = g.dfs(state_1, state_2)
    for state in path:
        print(state)
