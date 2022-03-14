# Implementation of the class Graph
class Graph:
    # Creation of the constructor with number of nodes, edges, and a dictionary to stores
    # the index of where the nodes belong.
    def __init__(self, num_of_nodes):
        # Start the number of nodes in the graph
        self.V = num_of_nodes
        # Start list of edges
        self.edges = []
        # Dictionary to store the index of the component it belongs
        self.node = {}

    # Function to add an Edge to a Graphs node
    # Use format: first, second, edge weight
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # Function to find a set of element n using path compression technique
    def find_node(self, n):
        if self.node[n] == n:
            return n
        return self.find_node(self.node[n])

    # Function to unify nodes into one by finding the roots.
    # Two nodes are given as input
    # We add the size of smaller component into the larger one,
    def join(self, node_size, u, v):
        # We add the size of smaller component into the larger one,
        if node_size[u] <= node_size[v]:
            self.node[u] = v
            node_size[v] += node_size[u]
        # and then add the size of the smaller one to the size of the larger one
        elif node_size[u] >= node_size[v]:
            self.node[v] = self.find_node(u)
            node_size[u] += node_size[v]

        # --> they become one
        print("New node=", self.node)

    # Main function needed to create the algorithm
    def boruvka(self):
        node_size = []
        mst_weight = 0
        # Array to store index of cheapest edges. Stores u,v,w respectively
        cheapest = [-1] * self.V
        num_of_trees = self.V

        # Create V subsets with single elements
        for node in range(self.V):
            self.node.update({node: node})
            node_size.append(1)

        # Keep combining components until all components
        # are not combined into a single MST
        while num_of_trees > 1:
            # Check all edges and update cheapest of every node
            for i in range(len(self.edges)):
                # Find nodes of the two sides on the current edge
                u = self.edges[i][0]
                v = self.edges[i][1]
                w = self.edges[i][2]
                node_u = self.node[u]
                node_v = self.node[v]

                # If two side of the current edge are from same set --> Ignore current edge
                # Else check if current edge is closer to previous cheapest edge of node_u and node_v
                if node_u != node_v:
                    if cheapest[node_u] == -1 or cheapest[node_u][2] > w:
                        cheapest[node_u] = [u, v, w]
                    if cheapest[node_v] == -1 or cheapest[node_v][2] > w:
                        cheapest[node_v] = [u, v, w]

            # Consider the above cheapest edges and add them to the MST
            for node in range(self.V):
                # Check if cheapest for set exists
                if cheapest[node] != -1:
                    u = cheapest[node][0]
                    v = cheapest[node][1]
                    w = cheapest[node][2]
                    node_u = self.node[u]
                    node_v = self.node[v]

                    # add the weight to the new node
                    if node_u != node_v:
                        mst_weight += w
                        self.join(node_size, node_u, node_v)
                        print("Edge", u,"-",v,"weight =", w)
                        num_of_trees -= 1

        # Solution of the problem
        print("Weight of the MSP is: " + str(mst_weight))


# Instructions to start the program
# Creation of the Graph
# Start of the program
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.boruvka()
