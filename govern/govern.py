import sys


#def main():
#    input_filename = "lngpok.in" if len(sys.argv) == 1 else sys.argv[1]
#    output_filename = "lngpok.out" if len(sys.argv) == 1 else sys.argv[2]
#
#    array = read_input(input_filename)
#    result = solve1(array)
#    write_output(output_filename, result)


#def read_input(filename):
#    with open(filename, "r") as input_file:
#        array_str = input_file.readline()
#        array = [int(item) for item in array_str.split()]
#        return array






def main():
    input_filename = "lngpok.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "lngpok.out" if len(sys.argv) == 1 else sys.argv[2]
    V,E = read_input(input_filename)

    graph = read_graph_from_file(input_filename, V, E)
    #try:
    #for vertex in get_topological_order(graph):
        #write_output(output_filename, V[vertex.label])
        #print vertex.label
    with open(output_filename, "w") as output_file:
        for vertex in get_topological_order(graph):
            output_file.write("%s\n" % V[vertex.label])
        #print vertex.label
    #except NotDirectedAcyclicGraphError:
        #print "The graph is not a directed acyclic graph (DAG)."

def read_input(filename):
    with open(filename, "r") as input_file:
        edges = 0
        arr = []
        for line in input_file:
            arr.append(str(line.split()[0]))
            arr.append(str(line.split()[1]))
            edges+=1
        #array_str = input_file.readline()
        #array = [int(item) for item in array_str.split()]
        #discount = int(input_file.readline())
        #print (list(set(arr)), edges)
        return list(set(arr)), edges

def write_output(filename, v):
    with open(filename, "w+") as output_file:
        output_file.write("%s\n" % str(v))

def find_list(l, el):
    pass


def read_graph_from_file(filename, vertex, edge_count):

    with open(filename, "r") as input_file:
        # The first two lines define the vertex count and the edge count.
        #vertex_count = int(input_file.readline())
        #edge_count = int(input_file.readline())

        vertices1 = [index for index in vertex]
        vertices = [Vertex(_) for _ in xrange(len(vertices1))]
        edges = []

        # The next 'edge_count' lines describe the edges: "start_vertex end_vertex".
        #print vertices1[1]
        for i in range(0, edge_count):
            start_vertex1, end_vertex1 = [index for index in input_file.readline().split()]
            start_vertex = vertices1.index(start_vertex1)
            end_vertex = vertices1.index(end_vertex1)
            #print start_vertex, end_vertex
            #print start_vertex1, end_vertex1
            # Adding the edge to the list of outbound edges for the start vertex.
            edge = Edge(vertices[start_vertex], vertices[end_vertex])
            vertices[start_vertex].outbound_edges.append(edge)
            edges.append(edge)

        return Graph(vertices, edges)


def get_topological_order(graph):
    return tarjan_dfs(graph, use_recursion=True)


def tarjan_dfs(graph, use_recursion=True):
    # Instead of keeping a boolean visited[] array, our visits will have 3 states.
    NOT_VISITED = 0
    VISITED = 1
    VISITED_AND_RESOLVED = 2

    topological_order = []
    topological_order_set = set()

    unvisited_vertices = set(graph.vertices)
    visited_status = [NOT_VISITED for vertex in graph.vertices]

    # A recursive, textbook implementation of Tarjan's DFS.
    def dfs_recursive(vertex):
        # We came across an unresolved dependency. It means there's a cycle in the graph.
        if visited_status[vertex.label] == VISITED:
            raise NotDirectedAcyclicGraphError

        if visited_status[vertex.label] == NOT_VISITED:
            unvisited_vertices.remove(vertex)
            visited_status[vertex.label] = VISITED

            # Getting all dependencies of the current vertex.
            neighbors = [edge.end_vertex for edge in vertex.outbound_edges]

            # Trying to recursively satisfy each dependency.
            for neighbor in neighbors:
                dfs_recursive(neighbor)

            # Marking this vertex as resolved and adding it to the order.
            visited_status[vertex.label] = VISITED_AND_RESOLVED
            topological_order.append(vertex)

    # An alternative stack-based implementation of DFS.
    # Particularly useful for Python due to its recursion limit.
    def dfs_stack(start_vertex):
        stack = [start_vertex]

        while len(stack) > 0:
            vertex = stack.pop()

            visited_status[vertex.label] = VISITED
            if vertex in unvisited_vertices:
                unvisited_vertices.remove(vertex)

            unvisited_neighbors = []
            for neighbor in [edge.end_vertex for edge in vertex.outbound_edges]:
                # We came across an unresolved dependency. It means there's a cycle in the graph.
                if visited_status[neighbor.label] == VISITED:
                    raise NotDirectedAcyclicGraphError
                # Getting all unexplored dependencies of the current vertex.
                if visited_status[neighbor.label] == NOT_VISITED:
                    unvisited_neighbors.append(neighbor)

            # If there are no more dependencies to explore, it means we've satisfied all of them
            # and we can add this vertex to the result of topological ordering.
            if len(unvisited_neighbors) == 0:
                visited_status[vertex.label] = VISITED_AND_RESOLVED
                # Avoid duplicates in the output.
                if vertex not in topological_order_set:
                    topological_order.append(vertex)
                    topological_order_set.add(vertex)
            else:
                # If there's something left to explore,
                # leaving the vertex in the stack along with all its neighbors.
                stack.append(vertex)
                stack.extend(unvisited_neighbors)

    # Using the stack-based implementation if the corresponding parameter was set.
    dfs_implementation = dfs_recursive if use_recursion else dfs_stack

    # Visit any unvisited vertex until there are no unvisited vertices left.
    while len(unvisited_vertices) > 0:
        dfs_implementation(next(iter(unvisited_vertices)))

    return topological_order


class NotDirectedAcyclicGraphError:
    def __init__(self):
        pass


class Vertex:
    def __init__(self, label):
        self.label = label
        self.outbound_edges = []

    def __str__(self):
        return "Label: %d    Edges: %s" % (self.label, ', '.join([str(edge) for edge in self.outbound_edges]))


class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

    def __str__(self):
        return "%d -> %d" % (self.start_vertex.label, self.end_vertex.label)


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges


if __name__ == "__main__":
    main()
