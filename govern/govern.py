import sys


def main():
    input_filename = "govern.in" if len(sys.argv) == 1 else sys.argv[1]
    output_filename = "govern.out" if len(sys.argv) == 1 else sys.argv[2]

    pairs = read_input(input_filename)
    certificate_order = solve(pairs)
    write_output(output_filename, certificate_order)


def read_input(filename):
    with open(filename, "r") as input_file:
        lines = input_file.readlines()
        return [line.split() for line in lines]


def solve(pairs):
    # Our problem represents a typical topological sorting problem on a graph
    # where the certificates are the vertices, and the outbound edges of each vertex
    # point to the prerequisite certificates. Let's construct the graph and sort it.
    graph = construct_graph(pairs)
    ordered_certificates = get_topological_order(graph)
    return ordered_certificates


def construct_graph(pairs):
    # Since we only care about labels and their dependent labels,
    # we won't even need Graph, Vertex and Edge objects.
    # Our graph will just be a dictionary of string -> set(string) pairs.
    graph = {}

    for certificate, prerequisite in pairs:
        if certificate not in graph:
            graph[certificate] = set()
        if prerequisite not in graph:
            graph[prerequisite] = set()
        graph[certificate].add(prerequisite)

    return graph


def get_topological_order(graph):
    return tarjan_dfs(graph)


def tarjan_dfs(graph):
    topological_order = []
    topological_order_set = set()
    unvisited_vertices = set(graph.keys())

    # An alternative stack-based implementation of Tarjan's DFS.
    # Particularly useful for Python due to its recursion limit.
    def dfs_stack(start_vertex):
        stack = [start_vertex]

        while len(stack) > 0:
            vertex = stack.pop()
            if vertex in unvisited_vertices:
                unvisited_vertices.remove(vertex)

            unvisited_neighbors = graph[vertex].intersection(unvisited_vertices)

            # If there are no more dependencies to explore, it means we've satisfied all of them
            # and we can add this vertex to the result of topological ordering.
            if len(unvisited_neighbors) == 0:
                # Avoid duplicates in the output.
                if vertex not in topological_order_set:
                    topological_order.append(vertex)
                    topological_order_set.add(vertex)
            else:
                # If there's something left to explore,
                # leaving the vertex in the stack along with all its neighbors.
                stack.append(vertex)
                stack.extend(unvisited_neighbors)

    # Visit any unvisited vertex until there are no unvisited vertices left.
    while len(unvisited_vertices) > 0:
        dfs_stack(unvisited_vertices.pop())

    return topological_order


def write_output(filename, certificate_order):
    with open(filename, "w") as output_file:
        for certificate in certificate_order:
            output_file.write("%s\n" % certificate)


if __name__ == "__main__":
    main()
